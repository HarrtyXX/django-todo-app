from django.forms import ModelForm
from .models import ToDoList, Item


class UpdateListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ["name"]


class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"