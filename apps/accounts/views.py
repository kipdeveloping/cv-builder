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

    from .models import SectorTag
    sectors = SectorTag.objects.all()
    return render(request, 'accounts/register.html', {'form': form, 'sectors': sectors})


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
        'es': 'Espanol', 'en': 'Ingles', 'pt': 'Portugues',
        'fr': 'Frances', 'de': 'Aleman', 'it': 'Italiano',
        'ja': 'Japones', 'ko': 'Coreano', 'zh': 'Chino',
        'ru': 'Ruso', 'ar': 'Arabe', 'hi': 'Hindi'
    }
    profile_lang_names = [LANG_NAMES.get(code, code) for code in profile.languages.keys()] if isinstance(profile.languages, dict) else []
    return render(request, 'accounts/dashboard.html', {
        'profile': profile,
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

    return render(request, 'accounts/profile.html', {
        'profile_user': user,
        'profile': profile,
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


@login_required
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

        if 'sector' in data:
            profile.sector = SectorTag.objects.get(slug=data['sector']) if data['sector'] else None
        if 'rol' in data:
            profile.rol = SectorRol.objects.get(slug=data['rol'], sector__slug=data['sector']) if data['rol'] else None
        if 'especialidad' in data:
            profile.especialidad = RolEspecialidad.objects.get(slug=data['especialidad'], sector_rol__slug=data['rol']) if data['especialidad'] else None
        if 'seniority' in data:
            profile.seniority = data['seniority']
        if 'languages' in data:
            langs = data['languages']
            if isinstance(langs, list):
                profile.languages = {l['code']: l.get('level', 'intermediate') for l in langs if l.get('code')}
            else:
                profile.languages = langs

        profile.save()

        if 'tags' in data:
            ProfileTag.objects.filter(profile=profile).delete()
            for tag_data in data['tags']:
                tag = Tag.objects.get(slug=tag_data['slug'])
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
            'name': pt.tag.name_es,
            'tag_type': pt.tag_type,
            'category': pt.tag.category
        } for pt in profile.tags.select_related('tag').all()]

        lang_names = {
            'es': 'Espanol', 'en': 'Ingles', 'pt': 'Portugues',
            'fr': 'Frances', 'de': 'Aleman', 'it': 'Italiano',
            'ja': 'Japones', 'ko': 'Coreano', 'zh': 'Chino',
            'ru': 'Ruso', 'ar': 'Arabe', 'hi': 'Hindi'
        }
        languages = [{'code': k, 'name': lang_names.get(k, k)} for k in profile.languages.keys()] if isinstance(profile.languages, dict) else []

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
