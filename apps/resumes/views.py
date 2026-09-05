from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext_lazy as _
import json

from .models import Resume, Template


@login_required
def select_template_view(request):
    templates = Template.objects.all()
    return render(request, 'resumes/select_template.html', {'templates': templates})


@login_required
@require_POST
def create_resume_view(request):
    template_id = request.POST.get('template_id')
    template = get_object_or_404(Template, id=template_id)

    resume = Resume.objects.create(
        user=request.user,
        template=template,
        status='draft',
        content={}
    )

    messages.success(request, _('CV creado exitosamente. ¡Ahora personalízalo!'))
    return redirect('editor', resume_id=resume.id)


@login_required
def editor_view(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    return render(request, 'resumes/editor.html', {'resume': resume})


@login_required
@require_POST
def save_resume_api(request):
    try:
        data = json.loads(request.body)
        resume_id = data.get('resume_id')
        content = data.get('content', {})

        resume = get_object_or_404(Resume, id=resume_id, user=request.user)
        resume.content = content
        resume.save()

        return JsonResponse({
            'status': 'ok',
            'timestamp': resume.updated_at.strftime('%H:%M')
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@login_required
@require_POST
def publish_resume_api(request):
    try:
        data = json.loads(request.body)
        resume_id = data.get('resume_id')
        tags = data.get('tags', [])
        primary_tag = data.get('primary_tag')

        resume = get_object_or_404(Resume, id=resume_id, user=request.user)

        if not resume.content.get('name') or not resume.content.get('bio'):
            return JsonResponse({
                'status': 'error',
                'message': 'Nombre y bio son obligatorios para publicar.'
            }, status=400)

        if not request.user.profile.photo:
            return JsonResponse({
                'status': 'error',
                'message': 'Debes subir una foto de perfil para publicar.'
            }, status=400)

        if not tags:
            return JsonResponse({
                'status': 'error',
                'message': 'Debes seleccionar al menos un sector.'
            }, status=400)

        from .models import SectorTag, ResumeTag

        primary_tag_id = primary_tag
        ResumeTag.objects.filter(resume=resume).delete()

        for tag_id in tags:
            tag = SectorTag.objects.get(id=tag_id)
            ResumeTag.objects.create(
                resume=resume,
                sector_tag=tag,
                is_primary=(tag_id == primary_tag_id)
            )

        if primary_tag_id:
            Resume.objects.filter(
                user=request.user,
                status='published',
                resume_tags__sector_tag_id=primary_tag_id,
                resume_tags__is_primary=True
            ).exclude(id=resume.id).update(status='draft')

        resume.status = 'published'
        resume.save()

        return JsonResponse({
            'status': 'ok',
            'resume_status': 'published'
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
