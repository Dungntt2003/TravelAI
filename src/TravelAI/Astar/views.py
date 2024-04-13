from django.shortcuts import render
from django.http import HttpResponse

# def Hello(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'homepage.html')

def Astar(request):
    return render(request, 'graph.html')