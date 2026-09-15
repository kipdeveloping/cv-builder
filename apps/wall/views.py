from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from apps.accounts.models import SectorTag, SectorRol, RolEspecialidad, Tag, UserProfile, ProfileTag


def landing_view(request):
    return render(request, 'landing.html')


def wall_view(request):
    return render(request, 'wall/wall.html')


def get_tag_hierarchy(request):
    sector_slug = request.GET.get('sector')
    lang = request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'es'

    sectors = SectorTag.objects.all()
    if sector_slug:
        sectors = sectors.filter(slug=sector_slug)

    hierarchy = []
    for sector in sectors:
        sector_data = {
            'id': sector.id,
            'slug': sector.slug,
            'name': sector.get_name(lang),
            'roles': []
        }

        for role in sector.roles.all():
            role_data = {
                'id': role.id,
                'slug': role.slug,
                'name': role.get_name(lang),
                'especialidades': []
            }

            for esp in role.especialidades.all():
                esp_data = {
                    'id': esp.id,
                    'slug': esp.slug,
                    'name': esp.get_name(lang),
                    'tags': []
                }

                for tag in esp.tags.all():
                    esp_data['tags'].append({
                        'id': tag.id,
                        'slug': tag.slug,
                        'name': tag.get_name(lang),
                        'category': tag.category
                    })

                role_data['especialidades'].append(esp_data)

            sector_data['roles'].append(role_data)

        hierarchy.append(sector_data)

    return JsonResponse({'hierarchy': hierarchy})


def wall_api_view(request):
    sector_slug = request.GET.get('sector')
    rol_slug = request.GET.get('rol')
    especialidad_slug = request.GET.get('especialidad')
    tags_must = request.GET.get('tags_must', '').split(',') if request.GET.get('tags_must') else []
    tags_nice = request.GET.get('tags_nice', '').split(',') if request.GET.get('tags_nice') else []
    seniority = request.GET.get('seniority')
    location = request.GET.get('location')
    languages = request.GET.get('languages')

    profiles = UserProfile.objects.filter(is_public=True).select_related(
        'user', 'sector', 'rol', 'especialidad'
    ).prefetch_related('tags__tag')

    if sector_slug:
        profiles = profiles.filter(sector__slug=sector_slug)
    if rol_slug:
        profiles = profiles.filter(rol__slug=rol_slug)
    if especialidad_slug:
        profiles = profiles.filter(especialidad__slug=especialidad_slug)
    if seniority:
        profiles = profiles.filter(seniority=seniority)
    if location:
        profiles = profiles.filter(location_flex=location)

    profile_list = []
    for profile in profiles:
        user = profile.user
        profile_tags = {pt.tag.slug: pt.tag_type for pt in profile.tags.all()}

        if tags_must:
            must_tags_set = set(tags_must)
            profile_must_tags = {slug for slug, ttype in profile_tags.items() if ttype == 'must'}
            if not must_tags_set.issubset(profile_must_tags):
                continue

        score = 0
        max_score = 0

        if sector_slug and profile.sector:
            score += 30
        max_score += 30 if sector_slug else 0

        if rol_slug and profile.rol:
            score += 25
        max_score += 25 if rol_slug else 0

        if especialidad_slug and profile.especialidad:
            score += 20
        max_score += 20 if especialidad_slug else 0

        for tag_slug in tags_must:
            max_score += 15
            if tag_slug in profile_tags and profile_tags[tag_slug] == 'must':
                score += 15

        for tag_slug in tags_nice:
            max_score += 10
            if tag_slug in profile_tags and profile_tags[tag_slug] == 'nice':
                score += 10

        relevance = round((score / max_score * 100) if max_score > 0 else 0)

        profile_list.append({
            'id': profile.id,
            'user_id': user.id,
            'name': user.get_full_name() or user.email,
            'headline': profile.headline or '',
            'bio': profile.bio or '',
            'photo': profile.photo.url if profile.photo else None,
            'sector': profile.sector.name_es if profile.sector else '',
            'rol': profile.rol.name_es if profile.rol else '',
            'especialidad': profile.especialidad.name_es if profile.especialidad else '',
            'seniority': profile.seniority or '',
            'location': profile.location_flex or '',
            'experience': profile.experience or [],
            'projects': profile.projects or [],
            'tags': profile_tags,
            'score': relevance,
        })

    profile_list.sort(key=lambda x: x['score'], reverse=True)

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


def get_all_tags_api(request):
    lang = request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'es'
    search = request.GET.get('search', '')

    tags = Tag.objects.all()
    if search:
        tags = tags.filter(
            Q(name_es__icontains=search) | Q(name_en__icontains=search)
        )

    tag_list = [{
        'id': tag.id,
        'slug': tag.slug,
        'name': tag.get_name(lang),
        'category': tag.category,
        'especialidad': tag.especialidad.name_es if tag.especialidad else None
    } for tag in tags[:50]]

    return JsonResponse({'tags': tag_list})
