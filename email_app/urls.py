from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("index", views.index, name="index"),
    path('list', views.list, name='list'),
    path('add', views.add, name='add'),
]
