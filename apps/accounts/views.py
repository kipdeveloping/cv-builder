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
                login(request, user)
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

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            from .models import UserProfile
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, _('¡Cuenta creada exitosamente!'))
            return redirect('dashboard')
        else:
            messages.error(request, _('Por favor, corrige los errores.'))
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, _('Has cerrado sesión correctamente.'))
    return redirect('landing')


@login_required
def dashboard_view(request):
    from apps.resumes.models import Resume
    user_resumes = Resume.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'accounts/dashboard.html', {
        'user_resumes': user_resumes,
        'profile': request.user.profile
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
