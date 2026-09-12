import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': 'tu@email.com'
        })
    )
    password = forms.CharField(
        label=_('Contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': '••••••••'
        })
    )


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'placeholder': 'tu@email.com'
        })
    )
    password1 = forms.CharField(
        label=_('Contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'placeholder': '••••••••'
        })
    )
    password2 = forms.CharField(
        label=_('Confirmar contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'placeholder': '••••••••'
        })
    )

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError(_('Este email ya está registrado.'))
        return email

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        errors = []

        if len(password) < 8:
            errors.append(_('La contraseña debe tener al menos 8 caracteres.'))
        if not re.search(r'[A-Z]', password):
            errors.append(_('La contraseña debe contener al menos una letra mayúscula.'))
        if not re.search(r'[0-9]', password):
            errors.append(_('La contraseña debe contener al menos un número.'))
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append(_('La contraseña debe contener al menos un carácter especial (!@#$%^&*(),.?":{}|<>).'))

        if errors:
            raise ValidationError(errors)
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class WizardRegistrationForm(RegistrationForm):
    first_name = forms.CharField(
        label=_('Nombre'),
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'placeholder': 'Tu nombre'
        })
    )
    last_name = forms.CharField(
        label=_('Apellido'),
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'placeholder': 'Tu apellido'
        })
    )
    title = forms.CharField(
        label=_('Cargo / Título profesional'),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'placeholder': 'Ej: Ingeniero de Software'
        })
    )
    sector = forms.CharField(
        label=_('Sector'),
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'placeholder': 'Ej: Tecnología'
        })
    )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        if commit:
            user.save()
            from .models import UserProfile, SectorTag
            profile = user.profile
            profile.title = self.cleaned_data.get('title', '')
            sector_name = self.cleaned_data.get('sector', '').strip()
            if sector_name:
                sector_obj, _ = SectorTag.objects.get_or_create(name=sector_name)
                profile.sector = sector_obj
            profile.save()
        return user
