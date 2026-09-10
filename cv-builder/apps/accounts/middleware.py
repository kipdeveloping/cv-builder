from django.urls import reverse
from django.shortcuts import redirect

ALLOWED_PREFIXES = (
    '/accounts/login/',
    '/accounts/register/',
    '/accounts/logout/',
    '/accounts/complete-profile/',
    '/accounts/google/',
    '/accounts/github/',
    '/accounts/microsoft/',
    '/accounts/apple/',
    '/accounts/3rdparty/',
    '/accounts/social/',
    '/set_language/',
    '/admin/',
    '/static/',
    '/media/',
)


class EnsureProfileMiddleware:
    """
    Fuerza a los usuarios autenticados a completar su perfil profesional
    (título o sector) antes de acceder al resto de secciones. Sucede
    principalmente tras un registro/login social, que no pasa por el wizard.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            path = request.path
            if not path.startswith(ALLOWED_PREFIXES):
                try:
                    profile = request.user.profile
                    complete = bool(profile.title or profile.sector_id)
                except Exception:
                    complete = False
                if not complete:
                    request.session['profile_next'] = path
                    return redirect(reverse('complete_profile'))
        return self.get_response(request)