from django.urls import path, include
from rest_framework import routers
from .views import login, register, UserViewSet

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),

]
