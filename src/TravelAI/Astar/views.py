from django.shortcuts import redirect, render
from .forms import MyForm
from .algorithm.Astar import Graph
from .algorithm.dataDis import road_distances
# from .models import Student

def register(request):
    # username & password
    return render(request, 'register.html')
def login(request):
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


