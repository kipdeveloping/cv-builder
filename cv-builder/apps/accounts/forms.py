import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.resumes.models import SectorTag


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
    first_name = forms.CharField(
        label=_('Nombre'),
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': _('Tu nombre')
        })
    )
    last_name = forms.CharField(
        label=_('Apellido'),
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': _('Tus apellidos')
        })
    )
    email = forms.EmailField(
        label=_('Email'),
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': 'tu@email.com'
        })
    )
    password1 = forms.CharField(
        label=_('Contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': '••••••••'
        })
    )
    password2 = forms.CharField(
        label=_('Confirmar contraseña'),
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': '••••••••'
        })
    )
    title = forms.CharField(
        label=_('Título profesional'),
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500',
            'placeholder': _('Ej: Desarrollador Web')
        })
    )
    sector = forms.ModelChoiceField(
        queryset=SectorTag.objects.all(),
        required=False,
        widget=forms.HiddenInput(),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

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

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', _('Las contraseñas no coinciden.'))

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.first_name = self.cleaned_data.get('first_name', '').strip()
        user.last_name = self.cleaned_data.get('last_name', '').strip()
        if commit:
            user.save()
        return user
