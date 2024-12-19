from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.home_view, name='index'),
    path('shopping-bag/', views.shopping_bag, name='shopping_bag'),
]
