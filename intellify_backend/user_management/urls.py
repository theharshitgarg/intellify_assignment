"""user_management URL Configuration

"""
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('login', views.LoginView.as_view(), name='login_view'),
    path('signup', views.SignUpView.as_view() , name='signup_view'),
]
