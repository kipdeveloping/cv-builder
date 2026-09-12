from django.contrib import admin
from .models import Template, Resume, SectorTag, ResumeTag


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'slug']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['user', 'template', 'status', 'updated_at', 'created_at']
    list_filter = ['status', 'template', 'created_at', 'updated_at']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    raw_id_fields = ['user', 'template']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(SectorTag)
class SectorTagAdmin(admin.ModelAdmin):
    list_display = ['name_es', 'name_en', 'slug']
    prepopulated_fields = {'slug': ('name_es',)}
    search_fields = ['name_es', 'name_en']


@admin.register(ResumeTag)
class ResumeTagAdmin(admin.ModelAdmin):
    list_display = ['resume', 'sector_tag', 'is_primary']
    list_filter = ['is_primary', 'sector_tag']
    search_fields = ['resume__user__email', 'sector_tag__name_es']
    raw_id_fields = ['resume', 'sector_tag']
