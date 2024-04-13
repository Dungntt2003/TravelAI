from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('homepage/', views.homepage),
    path('graph/', views.Astar),
]