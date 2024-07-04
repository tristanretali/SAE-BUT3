from django.test import TestCase
from recipe.models import Ingredient,Recipe,Cuisine,Equipment,Step,AnalyzedInstruction
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .serializers import RecipeSerializer

class RESTTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # self.pascal = User.objects.create_user('pascal', 'pascal@test.com', 'pascal')
        # make all request authenticated by default
        #self.client.force_authenticate(user=self.pascal)
        # store 3 articles in test database
        # self.article1 = Article.objects.create(titre="Test Titre", contenu="Test Contenu")
        # self.article2 = Article.objects.create(titre="Test Titre 2", contenu="Test Contenu 2")
        # self.article3 = Article.objects.create(titre="Article 3", contenu="Contenu 3")

    def test_list_articles(self):
        response = self.client.get('/rest/recipes/search?title=chicken')
        print(response)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        # articles = Article.objects.all().order_by('titre')
        # serializer_data = ArticleSerializer(articles, many=True).data
        # self.assertEqual(response.data, serializer_data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.client.force_authenticate(user=None)

    # def test_get_article(self):
    #     # get article with id 1
    #     response = self.client.get("/rest/articles/1/")
    #     # compare content with article1
    #     serializer_data = ArticleSerializer(self.article1).data
    #     self.assertEqual(response.data, serializer_data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.client.force_authenticate(user=None)

    # def test_post_article(self):
    #     new_data = {'titre': 'Nouveau Titre', 'contenu': 'Nouveau Contenu'}
    #     response = self.client.post("/rest/articles/", new_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.client.force_authenticate(user=None)

    # def test_modify_article(self):
    #     new_data = {'titre': 'Nouveau Titre', 'contenu': 'Nouveau Contenu'}
    #     # update article with id 1 with new_data
    #     response = self.client.put("/rest/articles/1/", data=new_data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.article1.refresh_from_db() # refresh article1 with data from database 
    #     self.assertEqual(self.article1.titre, new_data['titre'])
    #     self.assertEqual(self.article1.contenu, new_data['contenu'])
    #     self.client.force_authenticate(user=None)

    # def test_delete_article(self):
    #     # delete article with id 1
    #     response = self.client.delete("/rest/articles/1/")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     # check that article does not exist anymore in database        
    #     with self.assertRaises(Article.DoesNotExist):
    #         Article.objects.get(id=self.article1.id)
    #     self.client.force_authenticate(user=None)


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
