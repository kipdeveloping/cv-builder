from django.contrib import admin
from .models import UserProfile, SectorTag


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'headline', 'search_status', 'availability']
    list_filter = ['search_status', 'availability', 'location_flex']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'headline']


@admin.register(SectorTag)
class SectorTagAdmin(admin.ModelAdmin):
    list_display = ['name_es', 'name_en', 'slug']
    search_fields = ['name_es', 'name_en']
    prepopulated_fields = {'slug': ('name_es',)}
