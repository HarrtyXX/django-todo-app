from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import *

# Create your views here.

def home(request):
    all_list = ToDoList.objects.all()
    
    context = {"all_list": all_list}
    return render(request, 'todo/home.html', context)


def create_list(request):
    if request.method == "POST":
        form = CreateListForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        form = CreateListForm()


    context = {"form": form}
    return render(request, 'todo/create_list.html', context)


def show_list(request, id):
    todo_list = ToDoList.objects.get(id=id)

    context = {"list":todo_list}
    return render(request, 'todo/show_list.html', context)


def edit_list(request, id):
    todo_list = ToDoList.objects.get(id=id)

    if request.method == "POST":
        form = UpdateListForm(request.POST, instance=todo_list)
        if form.is_valid:
            form.save()     
            return redirect('show_list', id=id)       
    else:
        form = UpdateListForm(instance=todo_list)


    context = {"form":form, "id": id}
    return render(request, 'todo/edit_list.html', context)


def add_item(request, id):
    todo_list = ToDoList.objects.get(id=id)
    form = AddItemForm(initial={"list": id})

    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('show_list', id=id)    

    context = {"form": form, "id": id}
    return render(request, 'todo/add_item.html', context)



def edit_item(request, id):
    item = Item.objects.get(id=id)
    list_id = item.list.id

    if request.method == "POST":
        form = UpdateItemForm(request.POST, instance = item)
        if form.is_valid:
            form.save()
            return redirect("show_list", id=list_id)
    else:
        form = UpdateItemForm(instance=item)


    context = {"form":form}
    return render(request, "todo/edit_item.html", context)


def delete_item(request, id):
    item = Item.objects.get(id=id)
    list_id = item.list.id

    item.delete()
    
    return redirect("show_list", id=list_id)