from django.db import models
from django.contrib.auth.models import User


class Template(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='template-thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'


class Resume(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Borrador'),
        ('published', 'Publicado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    content = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Resume of {self.user.email} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
        ordering = ['-updated_at']


class SectorTag(models.Model):
    name_es = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name_es

    def get_name(self, language='es'):
        if language == 'en':
            return self.name_en
        if language == 'es':
            return self.name_es
        return self.name_en

    class Meta:
        verbose_name = 'Sector Tag'
        verbose_name_plural = 'Sector Tags'


class ResumeTag(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='resume_tags')
    sector_tag = models.ForeignKey(SectorTag, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.resume} - {self.sector_tag}"

    class Meta:
        verbose_name = 'Resume Tag'
        verbose_name_plural = 'Resume Tags'
        unique_together = ['resume', 'sector_tag']
