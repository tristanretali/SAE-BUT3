from django.urls import path, include
from rest_framework import routers
from .views import login, register, logout, me

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('me/', me, name='me')
]
