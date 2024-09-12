from django.urls import path
from .views import ResumeExtractView
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('api/extract_resume/', ResumeExtractView.as_view(), name='extract-resume'),
]


