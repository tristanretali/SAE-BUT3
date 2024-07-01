from django.db import models
from wagtail.fields import StreamField
from wagtail.blocks import CharBlock, StructBlock, ListBlock, IntegerBlock, TextBlock

class Ingredient(models.Model):
    ingredient_id = models.IntegerField()
    aisle = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True)
    nameClean = models.CharField(max_length=255)
    amount = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.nameClean

class RecipePage(models.Model):
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    cheap = models.BooleanField(default=False)
    healthScore = models.IntegerField(default=0)
    title = models.CharField(max_length=255)  # Utilisation du champ title
    readyInMinutes = models.IntegerField(null=True, blank=True)
    servings = models.IntegerField(null=True, blank=True)
    image = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    summary = models.TextField(blank=True, null=True)
    cuisines = StreamField([
        ('cuisine', CharBlock(required=True)),
    ], blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    analyzedInstructions = StreamField([
        ('instruction', StructBlock([
            ('name', CharBlock(required=True)),
            ('steps', ListBlock(StructBlock([
                ('number', IntegerBlock(required=True)),
                ('step', TextBlock(required=True)),
            ]))),
        ])),
    ], blank=True, null=True)



