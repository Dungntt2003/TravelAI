from django.shortcuts import redirect, render
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

def login(request):
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'homepage.html')

def Astar(request):
    return render(request, 'graph.html')

def about(request):
    return render(request, 'about.html')


