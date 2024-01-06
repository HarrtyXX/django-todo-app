from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list/create', views.create_list, name="create_list"),
    path('list/<int:id>', views.show_list, name="show_list"),
    path('list/<int:id>/edit', views.edit_list, name="edit_list"),
    path('list/<int:id>/add', views.add_item, name="add_item"),

    path('item/<int:id>/edit', views.edit_item, name="edit_item"),
    path('item/<int:id>/delete', views.delete_item, name="delete_item"),
]
