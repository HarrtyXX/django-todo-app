from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name = models.TextField(max_length=200)
    owner = ...
class Item(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)