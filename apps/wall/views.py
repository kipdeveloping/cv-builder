from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from apps.resumes.models import Resume, SectorTag


def landing_view(request):
    return render(request, 'landing.html')


def wall_view(request):
    return render(request, 'wall/wall.html')


def wall_api_view(request):
    sector_slug = request.GET.get('sector')

    cvs = Resume.objects.filter(status='published').select_related('user', 'user__profile')

    if sector_slug:
        cvs = cvs.filter(resume_tags__sector_tag__slug=sector_slug, resume_tags__is_primary=True)

    cv_list = []
    for cv in cvs:
        profile = cv.user.profile
        content = cv.content or {}

        tags = []
        for resume_tag in cv.resume_tags.all():
            lang = request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'es'
            tags.append(resume_tag.sector_tag.get_name(lang))

        cv_list.append({
            'id': cv.id,
            'user_id': cv.user.id,
            'name': content.get('name', cv.user.get_full_name() or cv.user.email),
            'bio': profile.bio,
            'photo': profile.photo.url if profile.photo else None,
            'tags': tags,
            'template': cv.template.slug if cv.template else None,
        })

    return JsonResponse({'cvs': cv_list})


def get_tags_api(request):
    lang = request.LANGUAGE_CODE if hasattr(request, 'LANGUAGE_CODE') else 'es'
    tags = SectorTag.objects.all()
    tag_list = [{
        'id': tag.id,
        'slug': tag.slug,
        'name': tag.get_name(lang)
    } for tag in tags]
    return JsonResponse({'tags': tag_list})


def cv_detail_view(request, resume_id):
    cv = get_object_or_404(Resume, id=resume_id, status='published')
    return render(request, 'wall/cv_detail.html', {'cv': cv})
