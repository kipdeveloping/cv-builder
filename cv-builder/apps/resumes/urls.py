from django.urls import path
from . import views

urlpatterns = [
    path('editor/<int:resume_id>/', views.editor_view, name='editor'),
    path('select-template/', views.select_template_view, name='select_template'),
    path('create-resume/', views.create_resume_view, name='create_resume'),
    path('api/resume/save/', views.save_resume_api, name='save_resume'),
    path('api/resume/publish/', views.publish_resume_api, name='publish_resume'),
]
