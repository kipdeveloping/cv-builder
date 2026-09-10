from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .forms import RegistrationForm, CustomAuthenticationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
        else:
            messages.error(request, _('Email o contraseña incorrectos.'))
    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    from apps.resumes.models import SectorTag
    sectors = SectorTag.objects.all()
    lang = request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'es'
    sector_options = [{'id': s.id, 'name': s.get_name(lang)} for s in sectors]

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            from .models import UserProfile
            profile, created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    'title': form.cleaned_data.get('title', '').strip(),
                    'sector': form.cleaned_data.get('sector'),
                },
            )
            if form.cleaned_data.get('title') or form.cleaned_data.get('sector'):
                profile.title = form.cleaned_data.get('title', '').strip()
                profile.sector = form.cleaned_data.get('sector')
                profile.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, _('¡Cuenta creada exitosamente!'))
            return redirect('dashboard')
        else:
            messages.error(request, _('Por favor, corrige los errores.'))
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {
        'form': form,
        'sectors': sector_options,
    })


@login_required
def complete_profile_view(request):
    from apps.resumes.models import SectorTag
    profile = request.user.profile
    sectors = SectorTag.objects.all()
    lang = request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'es'
    sector_options = [{'id': s.id, 'name': s.get_name(lang)} for s in sectors]

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        sector_id = request.POST.get('sector')
        if not title and not sector_id:
            messages.error(request, _('Selecciona al menos un campo (título o sector).'))
        else:
            profile.title = title
            profile.sector_id = sector_id or None
            profile.save()
            next_url = request.session.pop('profile_next', None)
            return redirect(next_url or 'dashboard')

    return render(request, 'accounts/complete_profile.html', {
        'sectors': sector_options,
        'profile': profile,
    })


def logout_view(request):
    logout(request)
    messages.success(request, _('Has cerrado sesión correctamente.'))
    return redirect('landing')


@login_required
def dashboard_view(request):
    from apps.resumes.models import Resume
    user_resumes = Resume.objects.filter(user=request.user).order_by('-updated_at')
    from .models import UserProfile
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/dashboard.html', {
        'user_resumes': user_resumes,
        'profile': profile,
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
