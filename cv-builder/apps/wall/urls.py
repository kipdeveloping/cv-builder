from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('tablon/', views.wall_view, name='wall'),
    path('cv/<int:resume_id>/', views.cv_detail_view, name='cv_detail'),
    path('api/wall/cvs/', views.wall_api_view, name='wall_api'),
    path('api/tags/', views.get_tags_api, name='get_tags'),
]
