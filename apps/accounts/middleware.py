from django.shortcuts import redirect
from django.urls import reverse
from .models import UserProfile


class EnsureProfileMiddleware:
    EXEMPT_PATHS = ['/accounts/complete-profile/', '/accounts/login/', '/accounts/register/', '/accounts/logout/', '/admin/']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.path.startswith('/admin/'):
            if request.path not in self.EXEMPT_PATHS:
                try:
                    profile = request.user.profile
                    if not profile.title and not profile.sector:
                        return redirect('complete_profile')
                except UserProfile.DoesNotExist:
                    UserProfile.objects.create(user=request.user)
                    return redirect('complete_profile')

        response = self.get_response(request)
        return response
