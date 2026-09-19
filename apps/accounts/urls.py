from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('settings/', views.account_settings_view, name='account_settings'),
    path('upload-photo/', views.upload_photo_view, name='upload_photo'),
    path('upload-media/', views.upload_media_view, name='upload_media'),
    path('update-bio/', views.update_bio_view, name='update_bio'),
    path('update-profile/', views.update_profile_fields_view, name='update_profile_fields'),
    path('update-recruiter-profile/', views.update_recruiter_profile_view, name='update_recruiter_profile'),
    path('toggle-visibility/', views.toggle_profile_visibility, name='toggle_profile_visibility'),
    path('toggle-recruiter-visibility/', views.toggle_recruiter_visibility, name='toggle_recruiter_visibility'),
    path('create-vacancy/', views.create_vacancy_view, name='create_vacancy'),
    path('contact/<int:user_id>/', views.contact_email_view, name='contact_email'),
    path('api/profile/tags/', views.get_profile_tags_view, name='get_profile_tags'),
    path('api/profile/tags/save/', views.save_profile_tags_view, name='save_profile_tags'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html',
        success_url=reverse_lazy('password_change_done'),
    ), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html',
    ), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        success_url=reverse_lazy('password_reset_done'),
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html',
    ), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('password_reset_complete'),
    ), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html',
    ), name='password_reset_complete'),
    path('empresa/<int:user_id>/', views.recruiter_profile_view, name='recruiter_profile'),
]
