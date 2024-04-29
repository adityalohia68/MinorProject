from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("", views.loginUser, name="login"),
    path("book", views.bookPage, name="book"),
    path("register", views.register, name="register"),
    path("docLogin", views.docLogin, name="docLogin"),
    path("docRegis", views.docRegis, name="docRegis"),
    path("manage", views.manage, name="manage"),
]
