from django.urls import path
from django.shortcuts import render, redirect
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
     path('', views.loginPage, name='login'),
     path('doLogin/', views.doLogin, name='doLogin'),
     path('addUser/', views.addUser, name='addUser'),
]