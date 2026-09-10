from django.shortcuts import redirect
from django.urls import reverse


class EnsureProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                profile = request.user.profile
                if not profile.title and not profile.sector:
                    if request.path != reverse('complete_profile'):
                        return redirect('complete_profile')
            except Exception:
                pass

        response = self.get_response(request)
        return response
