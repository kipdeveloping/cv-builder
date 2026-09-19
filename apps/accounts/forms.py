import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings


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
    role = forms.ChoiceField(
        label=_('Rol'),
        choices=[('candidate', 'Candidato'), ('recruiter', 'Reclutador')],
        required=False,
        initial='candidate',
        widget=forms.HiddenInput()
    )
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
    sector = forms.CharField(
        label=_('Sector'),
        max_length=100,
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white'
        })
    )
    # Recruiter-specific fields
    company_name = forms.CharField(
        label=_('Nombre de Empresa'),
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'placeholder': 'Nombre de tu empresa'
        })
    )
    company_type = forms.ChoiceField(
        label=_('Tipo de Empresa'),
        choices=[('', 'Seleccionar...'), ('empresa', 'Empresa'), ('particular', 'Particular')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white'
        })
    )
    work_modality = forms.ChoiceField(
        label=_('Modalidad'),
        choices=[('', 'Seleccionar...'), ('remote', 'Remoto'), ('hybrid', 'Híbrido'), ('onsite', 'Presencial')],
        required=False,
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white'
        })
    )
    company_website = forms.URLField(
        label=_('Sitio Web'),
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'placeholder': 'https://...'
        })
    )
    company_description = forms.CharField(
        label=_('Descripción de la Empresa'),
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white dark:bg-gray-700 text-gray-900 dark:text-white',
            'rows': 3,
            'placeholder': 'Cuéntanos sobre tu empresa...'
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import SectorTag
        sector_choices = [('', _('Seleccionar...'))]
        for tag in SectorTag.objects.all():
            sector_choices.append((tag.slug, tag.name_es))
        self.fields['sector'].choices = sector_choices

    def clean_email(self):
        email = self.cleaned_data.get('email')
        role = self.data.get('role') or self.cleaned_data.get('role') or 'candidate'
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            raise ValidationError(_('Este email ya está registrado.'))
        
        # Corporate email validation for recruiters
        if role == 'recruiter':
            domain = email.split('@')[-1].lower() if '@' in email else ''
            blocked_domains = getattr(settings, 'BLOCKED_EMAIL_DOMAINS', [])
            if domain in blocked_domains:
                raise ValidationError(_('Para registrarse como reclutador, debe usar un correo corporativo (no se permiten correos de dominios genéricos como Gmail, Yahoo, etc).'))
        
        return email

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role') or self.data.get('role') or 'candidate'
        cleaned_data['role'] = role

        if role == 'recruiter':
            company_name = cleaned_data.get('company_name', '').strip()
            if not company_name:
                self.add_error('company_name', _('El nombre de la empresa es obligatorio.'))

        sector = cleaned_data.get('sector', '').strip()
        if not sector:
            self.add_error('sector', _('Por favor, selecciona un sector.'))

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name', '').strip()
        user.last_name = self.cleaned_data.get('last_name', '').strip()
        role = self.cleaned_data.get('role') or 'candidate'
        
        if commit:
            user.save()
            
            # Keep UserProfile.role consistent for both roles
            user.profile.role = role
            
            if role == 'recruiter':
                from .models import RecruiterProfile, SectorTag
                profile = RecruiterProfile.objects.create(user=user)
                profile.company_name = self.cleaned_data.get('company_name', '').strip()
                profile.company_type = self.cleaned_data.get('company_type', '')
                profile.work_modality = self.cleaned_data.get('work_modality', '')
                profile.company_website = self.cleaned_data.get('company_website', '').strip()
                profile.company_description = self.cleaned_data.get('company_description', '').strip()
                sector_slug = self.cleaned_data.get('sector', '')
                if sector_slug:
                    try:
                        profile.company_sector = SectorTag.objects.get(slug=sector_slug)
                    except SectorTag.DoesNotExist:
                        pass
                profile.save()
            else:
                profile = user.profile
                sector_slug = self.cleaned_data.get('sector', '')
                if sector_slug:
                    from .models import SectorTag
                    try:
                        profile.sector = SectorTag.objects.get(slug=sector_slug)
                    except SectorTag.DoesNotExist:
                        pass
            
            user.profile.save()
        
        return user
