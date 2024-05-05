from django.shortcuts import redirect, render
# from .models import Student

def register(request):
    # username & password
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'homepage.html')

def Astar(request):
    return render(request, 'graph.html')


