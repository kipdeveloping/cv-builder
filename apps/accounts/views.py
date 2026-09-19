from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme
from django.db import transaction
from django.utils.text import slugify
import json
from .forms import CustomAuthenticationForm, WizardRegistrationForm
from .models import UserProfile, SectorTag, SectorRol, RolEspecialidad, Tag, ProfileTag, RecruiterProfile, Vacancy


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.GET.get('oauth_error'):
        messages.error(request, _('Este usuario no esta registrado. Por favor, crea una cuenta primero.'))

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                next_url = request.GET.get('next', 'dashboard')
                if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                    next_url = 'dashboard'
                return redirect(next_url)
        else:
            messages.error(request, _('Email o contrasena incorrectos.'))
    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {
        'form': form,
        'SOCIAL_AUTH_GOOGLE_OAUTH2_KEY': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        'SOCIAL_AUTH_GITHUB_KEY': settings.SOCIAL_AUTH_GITHUB_KEY,
        'SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY': settings.SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY,
    })


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    from .models import SectorTag
    if not SectorTag.objects.exists():
        from django.core.management import call_command
        try:
            call_command('loaddata', 'fixtures/sectors.json')
        except Exception:
            pass

    if request.method == 'POST':
        form = WizardRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, _('Cuenta creada exitosamente!'))
            return redirect('dashboard')
        else:
            messages.error(request, _('Por favor, corrige los errores.'))
    else:
        form = WizardRegistrationForm()

    sectors = SectorTag.objects.all()
    blocked_domains = getattr(settings, 'BLOCKED_EMAIL_DOMAINS', [])

    initial_step = 1
    if form.is_bound and not form.is_valid():
        if any(f in form.errors for f in ['email', 'password1', 'password2']):
            initial_step = 2
        elif any(f in form.errors for f in ['first_name', 'last_name', 'company_name', 'company_type']):
            initial_step = 3
        elif any(f in form.errors for f in ['sector', 'work_modality', 'company_website', 'company_description']):
            initial_step = 4
        else:
            initial_step = 2

    return render(request, 'accounts/register.html', {
        'form': form,
        'sectors': sectors,
        'blocked_domains': json.dumps(blocked_domains),
        'initial_step': initial_step,
    })


def logout_view(request):
    logout(request)
    messages.success(request, _('Has cerrado sesion correctamente.'))
    return redirect('landing')


@login_required
def dashboard_view(request):
    from .models import EMPLOYMENT_TYPE_CHOICES
    
    # Check user role and render appropriate dashboard
    try:
        recruiter_profile = RecruiterProfile.objects.get(user=request.user)
        return recruiter_dashboard_view(request, recruiter_profile)
    except RecruiterProfile.DoesNotExist:
        pass
    
    # Candidate dashboard
    profile = request.user.profile
    LANG_NAMES = {
        'es': _('Español'), 'en': _('Inglés'), 'pt': _('Portugués'),
        'fr': _('Francés'), 'de': _('Alemán'), 'it': _('Italiano'),
        'ja': _('Japonés'), 'ko': _('Coreano'), 'zh': _('Chino'),
        'ru': _('Ruso'), 'ar': _('Árabe'), 'hi': _('Hindi')
    }
    if isinstance(profile.languages, dict):
        profile_lang_names = [str(LANG_NAMES.get(code, code)) for code in profile.languages.keys() if code]
    elif isinstance(profile.languages, list):
        codes = [item['code'] if isinstance(item, dict) else item for item in profile.languages]
        profile_lang_names = [str(LANG_NAMES.get(code, code)) for code in codes if code]
    else:
        profile_lang_names = []
    return render(request, 'accounts/dashboard.html', {
        'profile': profile,
        'experience': profile.experience or [],
        'projects': profile.projects or [],
        'social_links': profile.social_links or {},
        'employment_types': EMPLOYMENT_TYPE_CHOICES,
        'profile_lang_names': profile_lang_names,
    })


@login_required
def recruiter_dashboard_view(request, recruiter_profile=None):
    if recruiter_profile is None:
        try:
            recruiter_profile = RecruiterProfile.objects.get(user=request.user)
        except RecruiterProfile.DoesNotExist:
            return redirect('dashboard')
    
    vacancies = recruiter_profile.vacancies.all()
    social_links = recruiter_profile.social_links or {}
    
    return render(request, 'accounts/recruiter_dashboard.html', {
        'recruiter_profile': recruiter_profile,
        'vacancies': vacancies,
        'social_links': social_links,
    })


@login_required
def create_vacancy_view(request):
    try:
        recruiter_profile = RecruiterProfile.objects.get(user=request.user)
    except RecruiterProfile.DoesNotExist:
        return redirect('dashboard')
    
    return render(request, 'accounts/create_vacancy.html', {
        'recruiter_profile': recruiter_profile,
    })


@login_required
def upload_photo_view(request):
    if request.method == 'POST' and request.FILES.get('photo'):
        photo = request.FILES['photo']

        if photo.size > 5 * 1024 * 1024:
            messages.error(request, _('La foto no puede superar los 5MB.'))
            return redirect('dashboard')

        allowed_types = ['image/jpeg', 'image/png', 'image/webp']
        if photo.content_type not in allowed_types:
            messages.error(request, _('Solo se permiten archivos JPG, PNG o WebP.'))
            return redirect('dashboard')

        profile = request.user.profile
        profile.photo = photo
        profile.save()
        messages.success(request, _('Foto actualizada correctamente.'))

    return redirect('dashboard')


@login_required
@require_POST
def upload_media_view(request):
    import os, uuid
    from django.core.files.storage import default_storage
    from django.core.files.base import ContentFile

    if 'image' not in request.FILES:
        return JsonResponse({'status': 'error', 'message': _('No se proporcionó ninguna imagen.')}, status=400)

    image = request.FILES['image']
    if image.size > 5 * 1024 * 1024:
        return JsonResponse({'status': 'error', 'message': _('La imagen no puede superar los 5MB.')}, status=400)

    allowed_types = ['image/jpeg', 'image/png', 'image/webp', 'image/gif', 'image/svg+xml']
    if image.content_type not in allowed_types:
        return JsonResponse({'status': 'error', 'message': _('Formato no permitido. Usa JPG, PNG, WebP o SVG.')}, status=400)

    ext = os.path.splitext(image.name)[1].lower()
    filename = f"media_items/user_{request.user.id}_{uuid.uuid4().hex[:8]}{ext}"
    saved_path = default_storage.save(filename, ContentFile(image.read()))
    url = default_storage.url(saved_path)

    return JsonResponse({'status': 'ok', 'url': url})


@login_required
def update_bio_view(request):
    if request.method == 'POST':
        bio = request.POST.get('bio', '')
        profile = request.user.profile
        profile.bio = bio
        profile.save()
        messages.success(request, _('Bio actualizada correctamente.'))

    return redirect('dashboard')



def recruiter_profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    try:
        recruiter_profile = RecruiterProfile.objects.get(user=user)
    except RecruiterProfile.DoesNotExist:
        from django.http import Http404
        raise Http404

    if not recruiter_profile.is_public:
        from django.http import Http404
        raise Http404

    vacancies = recruiter_profile.vacancies.filter(status='active')

    return render(request, 'accounts/recruiter_profile.html', {
        'profile_user': user,
        'recruiter_profile': recruiter_profile,
        'vacancies': vacancies,
    })

def profile_view(request, user_id):
    from django.http import Http404
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfile, user=user)

    if not profile.is_public:
        raise Http404

    is_owner = request.user.is_authenticated and request.user == user

    LANG_NAMES = {
        'es': _('Español'), 'en': _('Inglés'), 'pt': _('Portugués'),
        'fr': _('Francés'), 'de': _('Alemán'), 'it': _('Italiano'),
        'ja': _('Japonés'), 'ko': _('Coreano'), 'zh': _('Chino'),
        'ru': _('Ruso'), 'ar': _('Árabe'), 'hi': _('Hindi')
    }
    if isinstance(profile.languages, dict):
        profile_lang_names = [str(LANG_NAMES.get(code, code)) for code in profile.languages.keys() if code]
    elif isinstance(profile.languages, list):
        codes = [item['code'] if isinstance(item, dict) else item for item in profile.languages]
        profile_lang_names = [str(LANG_NAMES.get(code, code)) for code in codes if code]
    else:
        profile_lang_names = []

    return render(request, 'accounts/profile.html', {
        'profile_user': user,
        'profile': profile,
        'profile_lang_names': profile_lang_names,
        'is_owner': is_owner,
    })


@login_required
@require_POST
def update_profile_fields_view(request):
    try:
        data = json.loads(request.body)
        profile = request.user.profile

        if 'headline' in data:
            profile.headline = data['headline']
        if 'location_flex' in data:
            profile.location_flex = data['location_flex']
        if 'search_status' in data:
            profile.search_status = data['search_status']
        if 'availability' in data:
            profile.availability = data['availability']
        if 'bio' in data:
            profile.bio = data['bio']
        if 'experience' in data:
            profile.experience = data['experience']
        if 'projects' in data:
            profile.projects = data['projects']
        if 'social_links' in data:
            profile.social_links = data['social_links']
        if 'employment_type' in data:
            profile.employment_type = data['employment_type']
        if 'willing_to_relocate' in data:
            profile.willing_to_relocate = data['willing_to_relocate']
        if 'travel_availability' in data:
            profile.travel_availability = data['travel_availability']

        profile.save()

        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@login_required
@require_POST
def update_recruiter_profile_view(request):
    try:
        data = json.loads(request.body)
        recruiter_profile = RecruiterProfile.objects.get(user=request.user)

        if 'company_description' in data:
            recruiter_profile.company_description = data['company_description']
        if 'social_links' in data:
            recruiter_profile.social_links = data['social_links']

        recruiter_profile.save()

        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@login_required
@require_POST
def toggle_recruiter_visibility(request):
    try:
        recruiter_profile = RecruiterProfile.objects.get(user=request.user)
        recruiter_profile.is_public = not recruiter_profile.is_public
        recruiter_profile.save()

        return JsonResponse({
            'status': 'ok',
            'is_public': recruiter_profile.is_public
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@login_required
@require_POST
def toggle_profile_visibility(request):
    try:
        profile = request.user.profile

        if not profile.is_public and not profile.photo:
            return JsonResponse({
                'status': 'error',
                'message': 'Debes subir una foto de perfil para hacer tu perfil publico.'
            }, status=400)

        profile.is_public = not profile.is_public
        profile.save()

        return JsonResponse({
            'status': 'ok',
            'is_public': profile.is_public
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@require_POST
def contact_email_view(request, user_id):
    try:
        candidate = get_object_or_404(User, id=user_id)

        data = json.loads(request.body)
        sender_name = data.get('name', '').strip()
        sender_email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        if not sender_name or not sender_email or not message:
            return JsonResponse({
                'status': 'error',
                'message': 'Nombre, email y mensaje son obligatorios.'
            }, status=400)

        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(sender_email)
        except ValidationError:
            return JsonResponse({
                'status': 'error',
                'message': 'El formato del email no es valido.'
            }, status=400)

        candidate_name = candidate.get_full_name() or candidate.email
        subject = f'Contacto desde Perfil - {candidate_name}'

        email_body = f'Has recibido un mensaje desde la plataforma.\n\nDe: {sender_name}\nEmail: {sender_email}\n\nMensaje:\n{message}'

        send_mail(
            subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [candidate.email],
            fail_silently=False,
        )

        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@login_required
def account_settings_view(request):
    from social_django.models import UserSocialAuth

    social_accounts = UserSocialAuth.objects.filter(user=request.user)
    google_linked = social_accounts.filter(provider='google-oauth2').exists()
    github_linked = social_accounts.filter(provider='github').exists()
    linkedin_linked = social_accounts.filter(provider='linkedin-oauth2').exists()

    return render(request, 'accounts/account_settings.html', {
        'google_linked': google_linked,
        'github_linked': github_linked,
        'linkedin_linked': linkedin_linked,
    })


def oauth_complete(request, backend, *args, **kwargs):
    from social_core.exceptions import AuthException
    from social_django.views import complete as social_complete
    try:
        return social_complete(request, backend, *args, **kwargs)
    except AuthException:
        messages.error(request, _('Este usuario no esta registrado. Por favor, crea una cuenta primero.'))
        return redirect('login')


@login_required
@require_POST
def save_profile_tags_view(request):
    try:
        data = json.loads(request.body)
        profile = request.user.profile

        with transaction.atomic():
            if 'sector' in data:
                sector_slug = data.get('sector')
                profile.sector = SectorTag.objects.filter(slug=sector_slug).first() if sector_slug else None

            if 'rol' in data:
                rol_slug = data.get('rol')
                if rol_slug and profile.sector:
                    profile.rol = SectorRol.objects.filter(slug=rol_slug, sector=profile.sector).first()
                elif rol_slug:
                    profile.rol = SectorRol.objects.filter(slug=rol_slug).first()
                else:
                    profile.rol = None

            if 'especialidad' in data:
                esp_slug = data.get('especialidad')
                if esp_slug and profile.rol:
                    profile.especialidad = RolEspecialidad.objects.filter(slug=esp_slug, sector_rol=profile.rol).first()
                elif esp_slug:
                    profile.especialidad = RolEspecialidad.objects.filter(slug=esp_slug).first()
                else:
                    profile.especialidad = None

            if 'seniority' in data:
                profile.seniority = data.get('seniority', '') or ''

            if 'languages' in data:
                langs = data['languages']
                if isinstance(langs, list):
                    lang_dict = {}
                    for l in langs:
                        if isinstance(l, dict) and l.get('code'):
                            lang_dict[l['code']] = l.get('level', 'intermediate')
                        elif isinstance(l, str) and l.strip():
                            lang_dict[l.strip()] = 'intermediate'
                    profile.languages = lang_dict
                elif isinstance(langs, dict):
                    profile.languages = langs

            profile.save()

            if 'tags' in data:
                ProfileTag.objects.filter(profile=profile).delete()
                for tag_data in data['tags']:
                    raw_slug = tag_data.get('slug') or ''
                    raw_name = tag_data.get('name') or raw_slug
                    slug = (raw_slug or slugify(raw_name)).strip().lower()
                    name = (raw_name or slug).strip()
                    if slug:
                        tag = Tag.objects.filter(slug=slug).first()
                        if not tag:
                            tag = Tag.objects.create(
                                slug=slug,
                                name_es=name,
                                name_en=name,
                                category='otro'
                            )
                        ProfileTag.objects.create(
                            profile=profile,
                            tag=tag,
                            tag_type=tag_data.get('tag_type', 'nice')
                        )

        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@login_required
def get_profile_tags_view(request):
    try:
        profile = request.user.profile

        tags = [{
            'slug': pt.tag.slug,
            'name': pt.tag.display_name,
            'tag_type': pt.tag_type,
            'category': pt.tag.category
        } for pt in profile.tags.select_related('tag').all()]

        lang_names = {
            'es': str(_('Español')), 'en': str(_('Inglés')), 'pt': str(_('Portugués')),
            'fr': str(_('Francés')), 'de': str(_('Alemán')), 'it': str(_('Italiano')),
            'ja': str(_('Japonés')), 'ko': str(_('Coreano')), 'zh': str(_('Chino')),
            'ru': str(_('Ruso')), 'ar': str(_('Árabe')), 'hi': str(_('Hindi'))
        }
        if isinstance(profile.languages, dict):
            languages = [{'code': k, 'name': lang_names.get(k, k)} for k in profile.languages.keys() if k]
        elif isinstance(profile.languages, list):
            codes = [item['code'] if isinstance(item, dict) else item for item in profile.languages]
            languages = [{'code': c, 'name': lang_names.get(c, c)} for c in codes if c]
        else:
            languages = []

        return JsonResponse({
            'status': 'ok',
            'sector': profile.sector.slug if profile.sector else None,
            'rol': profile.rol.slug if profile.rol else None,
            'especialidad': profile.especialidad.slug if profile.especialidad else None,
            'seniority': profile.seniority,
            'languages': languages,
            'tags': tags
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
