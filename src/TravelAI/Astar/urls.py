from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('register/', views.register),
    path('register', register, name='register'),
    path('login/', views.login),
    path('homepage/', views.homepage),
    path('graph/', views.Astar),
    path('about/', views.about),
]