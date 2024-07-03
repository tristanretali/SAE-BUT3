from django.urls import path, include
from rest_framework import routers
from .views import get_ingredients_by_name,get_recipes_by_title

urlpatterns = [
    path('/search', get_recipes_by_title, name='recipes'),
    path('/ingredients', get_ingredients_by_name, name='ingredients')
]
