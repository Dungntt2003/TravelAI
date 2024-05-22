from django.shortcuts import redirect, render
# Rename imported function
from django.contrib.auth import authenticate, login as auth_login

# from .models import Student


def register(request):
    # username & password
    return render(request, 'register.html')


def user_login(request):  # Rename function
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the renamed import
            # Make sure this points to a defined URL name
            return redirect('homepage')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })
    else:
        return render(request, 'login.html')


def homepage(request):
    return render(request, 'homepage.html')


def Astar(request):
    return render(request, 'graph.html')
