from apps.accounts.models import UserProfile, RecruiterProfile
import requests
from django.core.files.base import ContentFile


def check_existing_user(backend, user, response, *args, **kwargs):
    if user is None:
        from django.http import HttpResponseRedirect
        from django.urls import reverse

        login_url = reverse('login')
        redirect_url = f'{login_url}?oauth_error=1'
        return HttpResponseRedirect(redirect_url)
    return {'user': user}


def save_user_profile(backend, user, response, *args, **kwargs):
    if user is None:
        return

    if backend.name == 'google-oauth2':
        first_name = response.get('given_name', '') or ''
        last_name = response.get('family_name', '') or ''
        photo_url = response.get('picture', '') or ''
    elif backend.name == 'github':
        name = (response.get('name') or '').split(' ', 1)
        first_name = name[0] if name else ''
        last_name = name[1] if len(name) > 1 else ''
        photo_url = response.get('avatar_url') or ''
    elif backend.name == 'linkedin-oauth2':
        first_name = response.get('firstName', {}).get('localized', {}).get('es_ES', '') or response.get('firstName', {}).get('localized', {}).get('en_US', '') or ''
        last_name = response.get('lastName', {}).get('localized', {}).get('es_ES', '') or response.get('lastName', {}).get('localized', {}).get('en_US', '') or ''
        picture = response.get('profilePicture', {}).get('displayImage', '') or ''
        photo_url = picture
    else:
        return

    if first_name and not user.first_name:
        user.first_name = first_name
    if last_name and not user.last_name:
        user.last_name = last_name
    user.save()

    # Check if user registered as recruiter via session
    is_recruiter = kwargs.get('request', {}).session.pop('oauth_role', None) == 'recruiter'
    
    if is_recruiter:
        RecruiterProfile.objects.get_or_create(user=user)
    else:
        profile, created = UserProfile.objects.get_or_create(user=user)

        if photo_url and not profile.photo:
            try:
                resp = requests.get(photo_url)
                if resp.status_code == 200:
                    photo_name = f'{user.username}_oauth.jpg'
                    profile.photo.save(photo_name, ContentFile(resp.content), save=True)
            except Exception:
                pass
