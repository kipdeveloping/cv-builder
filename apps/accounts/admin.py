from django.contrib import admin
from .models import UserProfile, SectorTag, SectorRol, RolEspecialidad, Tag, ProfileTag, RecruiterProfile, Vacancy


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'headline', 'search_status', 'availability', 'sector', 'rol', 'seniority']
    list_filter = ['search_status', 'availability', 'location_flex', 'sector', 'seniority']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'headline']


@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'user', 'company_sector', 'company_type', 'work_modality', 'is_public']
    list_filter = ['company_type', 'work_modality', 'is_public', 'company_sector']
    search_fields = ['company_name', 'user__email']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'recruiter_profile', 'modality', 'employment_type', 'status', 'applications_count']
    list_filter = ['status', 'modality', 'employment_type']
    search_fields = ['title', 'recruiter_profile__company_name']


@admin.register(SectorTag)
class SectorTagAdmin(admin.ModelAdmin):
    list_display = ['name_es', 'name_en', 'slug']
    search_fields = ['name_es', 'name_en']
    prepopulated_fields = {'slug': ('name_es',)}


@admin.register(SectorRol)
class SectorRolAdmin(admin.ModelAdmin):
    list_display = ['sector', 'name_es', 'name_en', 'slug']
    list_filter = ['sector']
    search_fields = ['name_es', 'name_en']
    prepopulated_fields = {'slug': ('name_es',)}


@admin.register(RolEspecialidad)
class RolEspecialidadAdmin(admin.ModelAdmin):
    list_display = ['sector_rol', 'name_es', 'name_en', 'slug']
    list_filter = ['sector_rol', 'sector_rol__sector']
    search_fields = ['name_es', 'name_en']
    prepopulated_fields = {'slug': ('name_es',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name_es', 'name_en', 'slug', 'category', 'especialidad']
    list_filter = ['category', 'especialidad']
    search_fields = ['name_es', 'name_en']
    prepopulated_fields = {'slug': ('name_es',)}


@admin.register(ProfileTag)
class ProfileTagAdmin(admin.ModelAdmin):
    list_display = ['profile', 'tag', 'tag_type']
    list_filter = ['tag_type', 'tag__category']
    search_fields = ['profile__user__email', 'tag__name_es']
