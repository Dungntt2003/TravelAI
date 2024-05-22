from django.urls import path
from . import views

urlpatterns = [
    # Add name for reversing
    path('register/', views.register, name='register'),
    # Update to renamed function and add name
    path('login/', views.user_login, name='login'),
    path('homepage/', views.homepage),
    path('graph/', views.Astar),
]
