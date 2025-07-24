
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("OK", status=200)


urlpatterns = [
    path("signup/", views.sign_up, name = 'signup'),
    path("health/", health_check, name="health"),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("home/",views.home, name ='home' ),
    path("home/add/",views.add_parents_and_students,name='add'),
    path('home/checkin/', views.checkin_view, name='checkin'),
    path('home/report/', views.report_page, name='report'),

    
]
