# Accounts URLS

from django.contrib import admin
from django.urls import path
from Accounts import views
urlpatterns = [
    path('login',views.User_login,name='user_login'),
    path('signup',views.Sign_up,name='signup'),
    path('logout',views.User_logout,name='logout')
    ]

