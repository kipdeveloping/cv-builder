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
from .models import UserProfile, UserSkill
from apps.resumes.models import Resume


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
            messages.error(request, _('Email o contraseña incorrectos.'))
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
            messages.success(request, _('¡Cuenta creada exitosamente!'))
            return redirect('dashboard')
        else:
            messages.error(request, _('Por favor, corrige los errores.'))
    else:
        form = WizardRegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, _('Has cerrado sesión correctamente.'))
    return redirect('landing')


@login_required
def dashboard_view(request):
    profile = request.user.profile
    user_resumes = Resume.objects.filter(user=request.user).order_by('-updated_at')

    featured_resume = profile.resume_destacado
    if not featured_resume or featured_resume.status != 'published':
        featured_resume = Resume.objects.filter(
            user=request.user, status='published'
        ).order_by('-updated_at').first()

    if not featured_resume and user_resumes.exists():
        featured_resume = user_resumes.first()

    experience = []
    projects = []
    social_links = {}
    if featured_resume:
        experience = featured_resume.content.get('experience', [])
        projects = featured_resume.content.get('projects', [])
        social_links = featured_resume.content.get('social_links', {})

    user_skills = UserSkill.objects.filter(user=profile).select_related('skill')

    return render(request, 'accounts/dashboard.html', {
        'profile': profile,
        'user_resumes': user_resumes,
        'featured_resume': featured_resume,
        'experience': experience,
        'projects': projects,
        'social_links': social_links,
        'user_skills': user_skills,
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


def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfile, user=user)

    featured_resume = profile.resume_destacado
    if not featured_resume or featured_resume.status != 'published':
        featured_resume = Resume.objects.filter(
            user=user, status='published'
        ).order_by('-updated_at').first()

    experience = []
    projects = []
    social_links = {}
    if featured_resume:
        experience = featured_resume.content.get('experience', [])
        projects = featured_resume.content.get('projects', [])
        social_links = featured_resume.content.get('social_links', {})

    user_skills = UserSkill.objects.filter(user=profile).select_related('skill')

    is_owner = request.user.is_authenticated and request.user == user

    return render(request, 'accounts/profile.html', {
        'profile_user': user,
        'profile': profile,
        'featured_resume': featured_resume,
        'experience': experience,
        'projects': projects,
        'social_links': social_links,
        'user_skills': user_skills,
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

        profile.save()

        return JsonResponse({'status': 'ok'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@login_required
@require_POST
def set_featured_resume_view(request):
    try:
        data = json.loads(request.body)
        resume_id = data.get('resume_id')

        profile = request.user.profile

        if resume_id:
            resume = get_object_or_404(Resume, id=resume_id, user=request.user)
            profile.resume_destacado = resume
        else:
            profile.resume_destacado = None

        profile.save()

        return JsonResponse({'status': 'ok'})
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
                'message': _('Nombre, email y mensaje son obligatorios.')
            }, status=400)

        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError
        try:
            validate_email(sender_email)
        except ValidationError:
            return JsonResponse({
                'status': 'error',
                'message': _('El formato del email no es valido.')
            }, status=400)

        candidate_name = candidate.get_full_name() or candidate.email
        subject = f'Contacto desde CV Builder - {candidate_name}'

        email_body = f"""
Has recibido un mensaje desde CV Builder.

De: {sender_name}
Email: {sender_email}

Mensaje:
{message}

---
Este mensaje fue enviado desde la plataforma CV Builder.
        """

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

    # Check which OAuth providers are linked
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
