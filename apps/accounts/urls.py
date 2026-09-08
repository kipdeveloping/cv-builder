from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('upload-photo/', views.upload_photo_view, name='upload_photo'),
    path('update-bio/', views.update_bio_view, name='update_bio'),
    path('update-profile/', views.update_profile_fields_view, name='update_profile_fields'),
    path('update-name/', views.update_name_view, name='update_name'),
    path('set-featured/', views.set_featured_resume_view, name='set_featured_resume'),
    path('contact/<int:user_id>/', views.contact_email_view, name='contact_email'),
]
