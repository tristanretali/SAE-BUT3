from django.db import models

class Ingredient(models.Model):
    ingredient_id = models.IntegerField()
    aisle = models.CharField(max_length=255)
    nameClean = models.CharField(max_length=255)
    amount = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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

class Recipe(models.Model):
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    cheap = models.BooleanField(default=False)
    healthScore = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    readyInMinutes = models.IntegerField(null=True, blank=True)
    servings = models.IntegerField(null=True, blank=True)
    image = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    summary = models.TextField(blank=True, null=True)
    cuisines = models.ManyToManyField(Cuisine, blank=True)
    instructions = models.TextField(blank=True, null=True)
    analyzedInstructions = models.ManyToManyField(AnalyzedInstruction, blank=True)

    def __str__(self):
        return self.title
