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


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    bio = models.TextField(blank=True, default='')
    headline = models.CharField(max_length=200, blank=True, default='')
    location_flex = models.CharField(max_length=20, choices=LOCATION_FLEX_CHOICES, blank=True, default='')
    search_status = models.CharField(max_length=20, choices=SEARCH_STATUS_CHOICES, blank=True, default='')
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, blank=True, default='')
    resume_destacado = models.ForeignKey('resumes.Resume', on_delete=models.SET_NULL, null=True, blank=True, related_name='featured_profiles')

    def __str__(self):
        return f"Profile of {self.user.email}"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            original_slug = self.slug
            counter = 1
            while Skill.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['name']


class UserSkill(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='user_skills')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.skill}"

    class Meta:
        verbose_name = 'User Skill'
        verbose_name_plural = 'User Skills'
        unique_together = ['user', 'skill']
