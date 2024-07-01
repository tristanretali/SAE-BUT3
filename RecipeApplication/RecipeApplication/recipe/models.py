from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class RecipePage(Page):
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    cheap = models.BooleanField(default=False)
    healthScore = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    readyInMinutes = models.IntegerField(null=True, blank=True)
    servings = models.IntegerField(null=True, blank=True)
    image = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    cuisines = StreamField([
        ('cuisine', blocks.CharBlock(required=True)),
    ], blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    analyzedInstructions = StreamField([
        ('instruction', blocks.StructBlock([
            ('name', blocks.CharBlock(required=True)),
            ('steps', blocks.ListBlock(blocks.StructBlock([
                ('number', blocks.IntegerBlock(required=True)),
                ('step', blocks.TextBlock(required=True)),
            ]))),
        ])),
    ], blank=True, null=True)

    # content_panels = Page.content_panels + [
    #     FieldPanel('vegetarian'),
    #     FieldPanel('vegan'),
    #     FieldPanel('cheap'),
    #     FieldPanel('healthScore'),
    #     FieldPanel('title'),
    #     FieldPanel('readyInMinutes'),
    #     FieldPanel('servings'),
    #     FieldPanel('image'),
    #     FieldPanel('summary'),
    #     FieldPanel('cuisines'),
    #     FieldPanel('instructions'),
    #     FieldPanel('analyzedInstructions'),
    #     InlinePanel('ingredients', label="Ingredients"),
    # ]


@register_snippet
class Ingredient(ClusterableModel):
    recipe = ParentalKey(RecipePage, on_delete=models.CASCADE, related_name='ingredients')
    ingredient_id = models.IntegerField()
    aisle = models.CharField(max_length=255)
    image = models.URLField(blank=True, null=True)
    nameClean = models.CharField(max_length=255)
    amount = models.FloatField()
    unit = models.CharField(max_length=50)

    # panels = [
    #     FieldPanel('ingredient_id'),
    #     FieldPanel('aisle'),
    #     FieldPanel('image'),
    #     FieldPanel('nameClean'),
    #     FieldPanel('amount'),
    #     FieldPanel('unit'),
    # ]

    def __str__(self):
        return self.nameClean
