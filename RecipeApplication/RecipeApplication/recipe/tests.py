from django.test import TestCase
from recipe.models import Ingredient,Recipe,Cuisine,Equipment,Step,AnalyzedInstruction
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Article
from .serializers import ArticleSerializer


class IngredientTests(TestCase):
    def setUp(self):
        # store 3 articles in test database
        Ingredient1 = Ingredient.objects.create(ingredient_id="1",aisle="meat", nameClean="Royal pouleto",amount="200",unit="g")
        Ingredient2 = Ingredient.objects.create(ingredient_id="2",aisle="vegetable", nameClean="Haricot",amount="100",unit="g")
        Ingredient3 = Ingredient.objects.create(ingredient_id="3",aisle="liquid", nameClean="milk",amount="10",unit="cl")

    def test_number_ingredient(self):
        """check that test articles are correctly identified"""
        ingredients = Ingredient.objects.filter(aisle__startswith="meat")
        self.assertEqual(ingredients.count(), 1)

    def test_create_article(self):
        """check that new article is correctly stored"""
        Ingredient.objects.create(ingredient_id="4",aisle="meat", nameClean="canard",amount="300",unit="g")
        ingredient = Ingredient.objects.get(nameClean="canard")
        self.assertEqual(ingredient.aisle, "meat")

    def test_delete_article(self):
        """check that test articles can be correctly deleted"""
        Ingredient.objects.filter(aisle__startswith="meat").delete() # remove 2 articles from 3
        ingredients = Ingredient.objects.all() # 1 article should be remaining
        self.assertEqual(ingredients.count(), 2)

class RecipeTests(TestCase):
    def setUp(self):
        # Create ingredients
        self.garlic = Ingredient.objects.create(ingredient_id=11215, aisle="Produce", nameClean="garlic", amount=2.0, unit="cloves")
        self.onion = Ingredient.objects.create(ingredient_id=11282, aisle="Produce", nameClean="onion", amount=1.0, unit="cup")

        # Create equipment
        self.frying_pan = Equipment.objects.create(name="frying pan")

        # Create steps
        self.step1 = Step.objects.create(number=1, step="Saute garlic and onion to the pan for 2 minutes")
        self.step1.ingredients.add(self.garlic, self.onion)
        self.step1.equipment.add(self.frying_pan)

        # Create analyzed instructions
        self.analyzed_instruction = AnalyzedInstruction.objects.create(name="Beef Toppings")
        self.analyzed_instruction.steps.add(self.step1)

        # Create cuisine
        self.cuisine = Cuisine.objects.create(name="Mexican")

        # Create recipe
        self.recipe = Recipe.objects.create(
            vegetarian=False,
            vegan=False,
            cheap=False,
            healthScore=100,
            title="Uber Nachos",
            readyInMinutes=45,
            servings=1,
            image="https://img.spoonacular.com/recipes/664208-556x370.jpg",
            summary="The recipe Uber Nachos can be made in approximately 45 minutes.",
            instructions="<ol><li>Saute garlic and onion to the pan for 2 minutes</li></ol>"
        )
        self.recipe.ingredients.add(self.garlic, self.onion)
        self.recipe.cuisines.add(self.cuisine)
        self.recipe.analyzedInstructions.add(self.analyzed_instruction)

    def test_recipe_creation(self):
        print(self.recipe)

        self.assertEqual(self.recipe.title, "Uber Nachos")
        self.assertEqual(self.recipe.healthScore, 100)
        self.assertFalse(self.recipe.vegetarian)
        self.assertIn(self.garlic, self.recipe.ingredients.all())
        self.assertIn(self.cuisine, self.recipe.cuisines.all())
        self.assertIn(self.analyzed_instruction, self.recipe.analyzedInstructions.all())

    def test_step_association(self):
        self.assertEqual(self.step1.number, 1)
        self.assertIn(self.garlic, self.step1.ingredients.all())
        self.assertIn(self.onion, self.step1.ingredients.all())
        self.assertIn(self.frying_pan, self.step1.equipment.all())
