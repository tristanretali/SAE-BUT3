from recipe.models import Recipe
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, null=False, unique=True)	
    password = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254)
    favorite_recipes = models.ManyToManyField(Recipe, blank=True)

    def __str__(self):
        return self.username
