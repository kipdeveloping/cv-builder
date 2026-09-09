from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import set_language
from apps.accounts.views import oauth_complete
from social_django import views as social_views
from social_django.urls import urlpatterns as social_urlpatterns

custom_social_urlpatterns = []
for p in social_urlpatterns:
    if p.name == 'complete':
        custom_social_urlpatterns.append(
            path('complete/<str:backend>/', oauth_complete, name='complete')
        )
    else:
        custom_social_urlpatterns.append(p)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set_language/', set_language, name='set_language'),
    path('social/', include((custom_social_urlpatterns, 'social'))),
    path('accounts/', include('apps.accounts.urls')),
    path('', include('apps.wall.urls')),
    path('', include('apps.resumes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
