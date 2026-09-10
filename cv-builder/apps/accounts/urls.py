from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('complete-profile/', views.complete_profile_view, name='complete_profile'),
    path('upload-photo/', views.upload_photo_view, name='upload_photo'),
    path('update-bio/', views.update_bio_view, name='update_bio'),
]
