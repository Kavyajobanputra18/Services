from django.contrib import admin
from django.urls import path, include
from user import views
from .views import UserLogin
from .views import UserSignIn


urlpatterns = [
    path('',views.index, name= 'index'),
    path('login/',UserLogin.as_view(), name = 'login'),
    path('register/',UserSignIn.as_view(), name = 'register'),


]