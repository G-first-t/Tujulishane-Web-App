
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", include("django.contrib.auth.urls"),),
    path("signup/", views.sign_up, name = 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("home/",views.home, name ='home' ),
    path("home/add/",views.add_parents_and_students,name='add')
    
]
