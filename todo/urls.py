from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('list/<int:id>', views.show_list, name="show_list")
]
