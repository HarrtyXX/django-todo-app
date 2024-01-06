from django.forms import ModelForm
from .models import ToDoList, Item


class CreateListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields =  "__all__"


class UpdateListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ["name"]


class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = "__all__"