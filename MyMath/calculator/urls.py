from django.urls import path, include

from . import views

urlpatterns = [
    path('logo/', views.logo),
    path('add/<int:a>/<int:b>/', views.add),
    path('subtract/<int:a>/<int:b>/', views.subtract),
    path('multiply/<int:a>/<int:b>/', views.multiply),
    path('divide/<int:a>/<int:b>/', views.divide)
]