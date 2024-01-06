from django.shortcuts import render
from .models import ToDoList

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')


def show_list(request, id):
    list = ToDoList.objects.get(id=id)

    context = {"list":list}
    return render(request, 'todo/list.html', context)