from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from apps.accounts.models import SectorTag, UserProfile


def landing_view(request):
    return render(request, 'landing.html')


def wall_view(request):
    return render(request, 'wall/wall.html')


def wall_api_view(request):
    sector_slug = request.GET.get('sector')

    profiles = UserProfile.objects.filter(is_public=True).select_related('user')

    if sector_slug:
        profiles = profiles.filter(sector_name__icontains=sector_slug)

    profile_list = []
    for profile in profiles:
        user = profile.user
        profile_list.append({
            'id': profile.id,
            'user_id': user.id,
            'name': user.get_full_name() or user.email,
            'headline': profile.headline or '',
            'bio': profile.bio or '',
            'photo': profile.photo.url if profile.photo else None,
            'sector': profile.sector_name or '',
            'location': profile.location_flex or '',
            'experience': profile.experience or [],
            'projects': profile.projects or [],
        })

    return JsonResponse({'profiles': profile_list})


def get_tags_api(request):
    lang = request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'es'
    tags = SectorTag.objects.all()
    tag_list = [{
        'id': tag.id,
        'slug': tag.slug,
        'name': tag.get_name(lang)
    } for tag in tags]
    return JsonResponse({'tags': tag_list})
