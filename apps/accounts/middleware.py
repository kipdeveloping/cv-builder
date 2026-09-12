from django.shortcuts import redirect
from django.urls import reverse
from .models import UserProfile


class EnsureProfileMiddleware:
    EXEMPT_PATHS = ['/accounts/login/', '/accounts/register/', '/accounts/logout/', '/admin/']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
