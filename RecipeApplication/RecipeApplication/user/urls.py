from django.urls import path, include
from rest_framework import routers
from .views import login, register, UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('api/', include(router.urls)),  # routes REST générées
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # route pour documentation API REST
]