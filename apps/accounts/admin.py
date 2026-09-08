from django.contrib import admin
from .models import UserProfile, Skill, UserSkill


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'headline', 'search_status', 'availability']
    list_filter = ['search_status', 'availability', 'location_flex']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'headline']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = ['user', 'skill', 'is_primary']
    list_filter = ['is_primary']
    search_fields = ['user__user__email', 'skill__name']
