from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    bio = models.TextField(blank=True, default='')

    def __str__(self):
        return f"Profile of {self.user.email}"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
