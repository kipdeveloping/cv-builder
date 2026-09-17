from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


LOCATION_FLEX_CHOICES = [
    ('remote', 'Remoto'),
    ('hybrid', 'Hibrido'),
    ('onsite', 'Presencial'),
]

SEARCH_STATUS_CHOICES = [
    ('active', 'Buscando activamente'),
    ('passive', 'Abierto a ofertas'),
    ('not_looking', 'No buscando'),
]

AVAILABILITY_CHOICES = [
    ('immediate', 'Inmediata'),
    ('2_weeks', '2 semanas'),
    ('1_month', '1 mes'),
    ('negotiable', 'Negociable'),
]

EMPLOYMENT_TYPE_CHOICES = [
    ('full_time', 'Full-time'),
    ('part_time', 'Part-time'),
    ('contract', 'Contrato'),
    ('freelance', 'Freelance'),
]

RELOCATE_CHOICES = [
    ('yes', 'Si'),
    ('no', 'No'),
    ('somewhere', 'Segun destino'),
]

TRAVEL_CHOICES = [
    ('none', 'No'),
    ('occasional', 'Ocasional'),
    ('frequent', 'Frecuente'),
]


def default_list():
    return []


class SectorTag(models.Model):
    name_es = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name_es

    def get_name(self, language='es'):
        return self.name_en if language == 'en' else self.name_es

    class Meta:
        verbose_name = 'Sector Tag'
        verbose_name_plural = 'Sector Tags'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    bio = models.TextField(blank=True, default='')
    headline = models.CharField(max_length=200, blank=True, default='')
    is_public = models.BooleanField(default=False)
    location_flex = models.CharField(max_length=20, choices=LOCATION_FLEX_CHOICES, blank=True, default='')
    search_status = models.CharField(max_length=20, choices=SEARCH_STATUS_CHOICES, blank=True, default='')
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, blank=True, default='')
    employment_type = models.JSONField(default=default_list, blank=True)
    willing_to_relocate = models.CharField(max_length=20, choices=RELOCATE_CHOICES, blank=True, default='')
    travel_availability = models.CharField(max_length=20, choices=TRAVEL_CHOICES, blank=True, default='')
    experience = models.JSONField(default=default_list, blank=True)
    projects = models.JSONField(default=default_list, blank=True)
    social_links = models.JSONField(default=dict, blank=True)
    sector = models.ForeignKey(SectorTag, on_delete=models.SET_NULL, null=True, blank=True)
    rol = models.ForeignKey('SectorRol', on_delete=models.SET_NULL, null=True, blank=True)
    especialidad = models.ForeignKey('RolEspecialidad', on_delete=models.SET_NULL, null=True, blank=True)

    SENIORITY_CHOICES = [
        ('junior', 'Junior'),
        ('semi_senior', 'Semi-Senior'),
        ('senior', 'Senior'),
        ('lead', 'Lead'),
    ]
    seniority = models.CharField(max_length=20, choices=SENIORITY_CHOICES, blank=True, default='')
    languages = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f'Profile of {self.user.email}'

    def get_employment_types_display(self):
        mapping = dict(EMPLOYMENT_TYPE_CHOICES)
        return ' | '.join(
            mapping.get(code, code) for code in (self.employment_type or []) if code
        )

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

class SectorRol(models.Model):
    sector = models.ForeignKey(SectorTag, on_delete=models.CASCADE, related_name='roles')
    name_es = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.sector.name_es} > {self.name_es}"

    def get_name(self, language='es'):
        return self.name_en if language == 'en' else self.name_es

    class Meta:
        unique_together = ('sector', 'slug')
        verbose_name = 'Sector Rol'
        verbose_name_plural = 'Sector Roles'


class RolEspecialidad(models.Model):
    sector_rol = models.ForeignKey(SectorRol, on_delete=models.CASCADE, related_name='especialidades')
    name_es = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.sector_rol} > {self.name_es}"

    def get_name(self, language='es'):
        return self.name_en if language == 'en' else self.name_es

    class Meta:
        unique_together = ('sector_rol', 'slug')
        verbose_name = 'Rol Especialidad'
        verbose_name_plural = 'Rol Especialidades'


class Tag(models.Model):
    CATEGORY_CHOICES = [
        ('lenguaje', 'Lenguaje'),
        ('framework', 'Framework'),
        ('herramienta', 'Herramienta'),
        ('soft_skill', 'Soft Skill'),
        ('otro', 'Otro'),
    ]

    name_es = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='otro')
    especialidad = models.ForeignKey(
        RolEspecialidad,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tags'
    )

    def __str__(self):
        return self.name_es

    def get_name(self, language='es'):
        return self.name_en if language == 'en' else self.name_es

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class ProfileTag(models.Model):
    TAG_TYPE_CHOICES = [
        ('must', 'Obligatorio'),
        ('nice', 'Deseable'),
    ]

    profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    tag_type = models.CharField(max_length=4, choices=TAG_TYPE_CHOICES, default='nice')

    class Meta:
        unique_together = ('profile', 'tag')
        verbose_name = 'Profile Tag'
        verbose_name_plural = 'Profile Tags'

    def __str__(self):
        return f"{self.profile} - {self.tag.name_es} ({self.tag_type})"





