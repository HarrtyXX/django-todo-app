from django.forms import ModelForm
from .models import ToDoList


class UpdateListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = ["name"]
