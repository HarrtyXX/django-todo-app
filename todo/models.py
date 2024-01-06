from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDoList(models.Model):
    name = models.TextField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.text