from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login
from .forms import MyForm
from .algorithm.Astar import Graph
from .algorithm.dataFamousPlace import famousPlace
from .algorithm.dataDis import road_distances
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Astar_user
from .algorithm.ulities import filter_data_by_path

isLogin = 0

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re-password']

        if password!= re_password:
            return render(request, 'register.html', {'error': 'Mật khẩu không khớp'})
        
        if Astar_user.objects.filter(email = email).exists():
            return render(request, 'register.html', {'error': 'Email đã tồn tại'})
        user, created = Astar_user.objects.get_or_create(email=email, password=password)
        if created:
            print('A new user was created.')
        else:
            print('The user already exists.')
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):  # Rename function
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if Astar_user.objects.filter(email = email).exists():
            if Astar_user.objects.filter(password = password).exists():
                isLogin = 1
                # print(isLogin)
                return render(request,'homepage.html' )
            else: 
                return render(request,'login.html',  {'error': 'Sai mật khẩu'} )
        else:
            return render(request,'login.html',  {'error': 'Tài khoản chưa tồn tại, vui lòng đăng ký'} )
    else:
        return render(request, 'login.html')

def homepage(request):
    return render(request, 'homepage.html')


def Astar(request):
    data = [
          {
              "name": 'Tay Ninh',
              "value" : "Tây Ninh"
          },
          {
              "name": 'Vung Tau',
              "value" : "Vũng Tàu"
          },
          {
              "name": 'Ben Tre',
              "value" : "Bến Tre"
          },
          {
              "name": 'Phu Quoc',
              "value" : "Phú Quốc"
          },
          {
              "name": 'TP Ho Chi Minh',
              "value" : "TP Hồ Chí Minh"
          },
          {
              "name": 'Nha Trang',
              "value" : "Nha Trang"
          },
          {
              "name": 'Dong Thap',
              "value" : "Đồng Tháp"
          },
          {
              "name": 'Can Tho',
              "value" : "Cần Thơ"
          },
          {
              "name": 'Soc Trang',
              "value" : "Sóc Trăng"
          },
          {
              "name": 'Ca Mau',
              "value" : "Cà Mau"
          },
          {
              "name": 'Lang Son',
              "value" : "Lạng Sơn"
          },
          {
              "name": 'Cao Bang',
              "value" : "Cao Bang"
          },
          {
              "name": 'Ha Giang',
              "value" : "Hà Giang"
          },
          {
              "name": 'Lao Cai',
              "value" : "Lào Cai"
          },
          {
              "name": 'Lai Chau',
              "value" : "Lai Châu"
          },
          {
              "name": 'Dien Bien',
              "value" : "Điện Biên"
          },
          {
              "name": 'Son La',
              "value" : "Sơn La"
          },
          {
              "name": 'Phu Tho',
              "value" : "Phú Thọ"
          },
          {
              "name": 'Ha Noi',
              "value" : "Hà Nội"
          },
          {
              "name": 'Quang Ninh',
              "value" : "Quảng Ninh"
          },
          {
              "name": 'Hai Duong',
              "value" : "Hải Dương"
          },
          {
              "name": 'Hai Phong',
              "value" : "Hải Phòng"
          },
          {
              "name": 'Thai Binh',
              "value" : "Thái Bình"
          },
          {
              "name": 'Nam Dinh',
              "value" : "Nam Định"
          },
          {
              "name": 'Ninh Binh',
              "value" : "Ninh Bình"
          },
          {
              "name": 'Thanh Hoa',
              "value" : "Thanh Hóa"
          },
          {
              "name": 'Nghe An',
              "value" : "Nghệ An"
          },
          {
              "name": 'Quang Binh',
              "value" : "Quảng Bình"
          },
          {
              "name": 'Hue',
              "value" : "Huế"
          },
          {
              "name": 'Da Nang',
              "value" : "Đà Nẵng"
          }
    ]
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
        
            selected_option1 = form.cleaned_data['startCity']
            selected_option2 = form.cleaned_data['endCity']
            graph1 = Graph(road_distances)
            path = graph1.a_star_algorithm(selected_option1, selected_option2)
            name_value_map = {item["name"]: item["value"] for item in data}
            new_path = [name_value_map.get(name, name) for name in path]
            filter_data = filter_data_by_path(path, famousPlace)
            print(filter_data)
            context = {'form': form, 'path': new_path, 'dataList' : filter_data}
            return render(request, 'graph.html', context)
    else:
        form = MyForm()
        context = {'form': form}

    return render(request, 'graph.html', context)

def about(request):
    return render(request, 'about.html')

