from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list/<int:id>', views.show_list, name="show_list"),
    path('list/<int:id>/edit', views.edit_list, name="edit_list"),
    path('list/<int:id>/add', views.add_item, name="add_item")
]
