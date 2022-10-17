from atexit import register
import logging
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('register/',views.user_register,name='register'),
    path('login/',views.user_login,name='login'),
    path('',views.profile,name='profile')
    
]