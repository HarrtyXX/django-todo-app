from django.shortcuts import render
from .models import ToDoList
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')


def show_list(request, id):
    todo_list = ToDoList.objects.get(id=id)

    if request.method == "POST":
        form = UpdateListForm(request.POST, instance=todo_list)
        if form.is_valid:
            form.save()            
    else:
        form = UpdateListForm(instance=todo_list)

    context = {"form":form}
    return render(request, 'todo/list.html', context)