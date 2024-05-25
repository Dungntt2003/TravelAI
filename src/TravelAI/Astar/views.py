from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login

from .forms import MyForm
from .algorithm.Astar import Graph
from .algorithm.dataDis import road_distances
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.hashers import make_password
# from .models import Student
from .models import User

# class RegisterForm(forms.ModelForm):
#     re_password = forms.CharField(widget=forms.PasswordInput(), label="Nhập lại mật khẩu")
#     class Meta:
#         model = User
#         fields = ['email', 'password']
#         widgets = {'password': forms.PasswordInput(),}
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError('Email đã tồn tại. Vui lòng đăng nhập.')
#         return email
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         re_password = cleaned_data.get('re_password')

#         if password != re_password:
#             raise forms.ValidationError('Mật khẩu không khớp.')
#         # if User.objects.filter(email=email).exists():
#         #     raise forms.ValidationError('Email đã tồn tại. Vui lòng đăng nhập.')
#         return cleaned_data


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email đã tồn tại. Vui lòng đăng nhập.')
            return redirect('login')
        
        if password != re_password:
            messages.error(request, 'Mật khẩu không khớp.')
            return redirect('register')
        
        hashed_password = make_password(password)
        User.objects.create(email=email, password=hashed_password)
        messages.success(request, 'Đăng ký thành công. Vui lòng đăng nhập.')

        return redirect('login')
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
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
        
            selected_option1 = form.cleaned_data['startCity']
            selected_option2 = form.cleaned_data['endCity']
            graph1 = Graph(road_distances)
            path = graph1.a_star_algorithm(selected_option1, selected_option2)
            print(f"Option 1: {selected_option1}")
            print(f"Option 2: {selected_option2}")
            print(path)
            context = {'form': form, 'path': path}
            return render(request, 'graph.html', context)
    else:
        form = MyForm()
        context = {'form': form}

    return render(request, 'graph.html', context)

def about(request):
    return render(request, 'about.html')

