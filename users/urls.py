from django.urls import path
from . import views

app_name = "users"

urlpatterns = (
    path('Settings/', views.settings),
    path('Profile/<slug:username>', views.profile),
    path('Login/', views.loginpage),
    path('Logout/', views.logoutuser),
    path('Register/', views.register),
    path('RegisterComplete/', views.registercomplete),
    path('Club/<slug:username>', views.clubprofile),
    path('Club/<slug:username>/Detail', views.clubdetail)
)
