from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from django.contrib.auth.models import User


class Ingredient(models.Model):
    ingredient_id = models.IntegerField()
    aisle = models.CharField(max_length=255)
    nameClean = models.CharField(max_length=255)
    amount = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.nameClean


class Equipment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Step(models.Model):
    number = models.IntegerField()
    step = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    equipment = models.ManyToManyField(Equipment, blank=True)
    length_number = models.IntegerField(blank=True, null=True)
    length_unit = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Step {self.number}: {self.step[:50]}"


class AnalyzedInstruction(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    steps = models.ManyToManyField(Step, blank=True)

    def __str__(self):
        return self.name or "Instruction"


class Cuisine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


@register_snippet
class Recipe(models.Model):
    vegetarian = models.BooleanField(default=False, verbose_name="Vegetarian?")
    vegan = models.BooleanField(default=False, verbose_name="Vegan?")
    cheap = models.BooleanField(default=False, verbose_name="Cheap?")
    healthScore = models.IntegerField(default=0, verbose_name="Health Score")
    title = models.CharField(max_length=255, verbose_name="Name of the recipe")
    readyInMinutes = models.IntegerField(null=True, blank=True, verbose_name="Time to prepare (in minutes)")
    servings = models.IntegerField(null=True, blank=True, verbose_name="Number of servings")
    image = models.TextField(blank=True, null=True, verbose_name="Image URL")
    ingredients = models.ManyToManyField(Ingredient, verbose_name="Ingredients")
    summary = models.TextField(blank=True, null=True, verbose_name="Summary")
    cuisines = models.ManyToManyField(Cuisine, blank=True, verbose_name="Cuisines")
    instructions = models.TextField(blank=True, null=True, verbose_name="Instructions")
    analyzedInstructions = models.ManyToManyField(AnalyzedInstruction, blank=True, verbose_name="Analyzed Instructions")

    def __str__(self):
        return self.title

    panels = [
        FieldPanel('vegetarian'),
        FieldPanel('vegan'),
        FieldPanel('cheap'),
        FieldPanel('healthScore'),
        FieldPanel('title'),
        FieldPanel('readyInMinutes'),
        FieldPanel('servings'),
        FieldPanel('image'),
        FieldPanel('ingredients'),
        FieldPanel('summary'),
        FieldPanel('cuisines'),
        FieldPanel('instructions'),
    ]
