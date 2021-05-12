from django.contrib.auth import login
from django.urls import path

from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout, name='logout'),
]
