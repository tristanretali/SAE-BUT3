import json

from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

from .models import Recipe, Ingredient
from rest_framework import viewsets
from .serializers import RecipeSerializer,IngredientSerializer
from rest_framework.decorators import action

class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ingredient.objects.all().order_by('nameClean')
    serializer_class = IngredientSerializer
    @action(detail=False, methods=['get'])
    def search(self,request):
            try:
                nameClean = request.GET.get('name')
                if nameClean:
                    # Récupère les ingrédients qui contiennent 'nameClean' dans leur nom
                    ingredients = Ingredient.objects.filter(nameClean__icontains=nameClean)
                    # enleve tout ceux qui ont '' comme nomClean
                    ingredients = [ingredient for ingredient in ingredients if ingredient.nameClean != '']

                    # Crée une liste des noms d'ingrédients uniques
                    unique_ingredient_names = list(set([ingredient.nameClean for ingredient in ingredients]))

                    return JsonResponse({
                        'ingredients': [
                            {
                                'name': name,
                            }
                            for name in unique_ingredient_names
                        ]
                    })
                else:
                    return JsonResponse({"detail": "Missing 'nameClean' parameter"}, status=400)
            except Exception as e:
                return JsonResponse({"detail": f"Error getting ingredients by name: {str(e)}"}, status=500)


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Recipe.objects.all().order_by('title')
    serializer_class = RecipeSerializer
    @action(detail=False, methods=['get'])
    def search(self,request):
        try:
            title = request.GET.get('title')
            if title:
                # Récupère les recettes qui contiennent 'title' dans leur nom
                recipes = Recipe.objects.filter(title__icontains=title)
                # enleve tout ceux qui ont '' comme nom
                recipes = [recipe for recipe in recipes if recipe.title != '']

                # return the list of recipes
                return JsonResponse({
                    'recipes': [
                        {
                            'title': recipe.title,
                            'readyInMinutes': recipe.readyInMinutes,
                            'servings': recipe.servings,
                            'image': recipe.image,
                            'summary': recipe.summary,
                            'instructions': recipe.instructions,
                            'healthScore': recipe.healthScore,
                            'vegetarian': recipe.vegetarian,
                            'vegan': recipe.vegan,
                            'cheap': recipe.cheap,
                            'cuisines': [cuisine.name for cuisine in recipe.cuisines.all()],
                            'ingredients': [
                                {
                                    'name': ingredient.nameClean,
                                    'amount': ingredient.amount,
                                    'unit': ingredient.unit,
                                }
                                for ingredient in recipe.ingredients.all()
                            ],
                            'analyzedInstructions': [
                                {
                                    'name': analyzedInstruction.name,
                                    'steps': [
                                        {
                                            'number': step.number,
                                            'step': step.step,
                                            # show ingredient names, amounts and units
                                            'ingredients': [
                                                {
                                                    'name': ingredient.nameClean,
                                                    'amount': ingredient.amount,
                                                    'unit': ingredient.unit,
                                                }
                                                for ingredient in step.ingredients.all()
                                            ],
                                            'equipment': [equipment.name for equipment in step.equipment.all()],
                                            'length_number': step.length_number,
                                            'length_unit': step.length_unit,
                                        }
                                        for step in analyzedInstruction.steps.all()
                                    ]
                                }
                                for analyzedInstruction in recipe.analyzedInstructions.all()
                            ]
                        }
                        for recipe in recipes
                    ]
                })
            else:
                return JsonResponse({"detail": "Missing 'title' parameter"}, status=400)
        except Exception as e:
            return JsonResponse({"detail": f"Error getting recipes by title: {str(e)}"}, status=500)