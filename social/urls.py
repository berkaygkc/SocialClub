from django.urls import path
from . import views

app_name = "social"

urlpatterns = (
    path('', views.index),
    path('follow/<slug:username>', views.follow),
    path('unfollow/<slug:username>', views.unfollow)
)
