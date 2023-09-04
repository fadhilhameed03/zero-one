from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('explore/', views.projects, name='explore'),
]