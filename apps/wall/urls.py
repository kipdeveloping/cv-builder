from django.urls import path
from apps.accounts.views import profile_view
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('tablon/', views.wall_view, name='wall'),
    path('candidato/<int:user_id>/', profile_view, name='profile'),
    path('api/wall/profiles/', views.wall_api_view, name='wall_api'),
    path('api/tags/', views.get_tags_api, name='get_tags'),
    path('api/tags/hierarchy/', views.get_tag_hierarchy, name='get_tag_hierarchy'),
    path('api/tags/all/', views.get_all_tags_api, name='get_all_tags'),
]
