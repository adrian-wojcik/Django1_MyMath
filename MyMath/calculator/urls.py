from django.urls import path, include

from . import views

urlpatterns = [
    path('logo/', views.logo),
]