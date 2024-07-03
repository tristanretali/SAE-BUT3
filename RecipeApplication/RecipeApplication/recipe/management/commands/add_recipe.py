from django.core.management.base import BaseCommand
from recipe.models import Recipe, Ingredient, AnalyzedInstruction, Step, Cuisine, Equipment
from recipe.services import recover_api_data

class Command(BaseCommand):
    help = 'Ajoute une recette à la base de données'

    def handle(self, *args, **kwargs):
        recipes = recover_api_data.recover_one_hundred_recipes(0)
        for item in recipes:
            try:
                # Créez l'objet Recipe sans les champs ManyToMany
                recipe = Recipe(
                    vegetarian=item.get('vegetarian', False),
                    vegan=item.get('vegan', False),
                    cheap=item.get('cheap', False),
                    healthScore=item.get('healthScore', 0),
                    title=item.get('title', ''),
                    readyInMinutes=item.get('readyInMinutes'),
                    servings=item.get('servings'),
                    image=item.get('image'),
                    summary=item.get('summary', ''),
                    instructions=item.get('instructions', '')
                )
                
                # Sauvegardez l'objet Recipe pour lui attribuer un ID
                recipe.save()

                # Ajoutez les cuisines après avoir sauvegardé l'objet Recipe
                cuisines = item.get('cuisines', [])
                for cuisine_name in cuisines:
                    cuisine, created = Cuisine.objects.get_or_create(name=cuisine_name)
                    recipe.cuisines.add(cuisine)
                
                for ingredient_data in item.get('extendedIngredients', []):
                    ingredient_id = ingredient_data.get('id')
                    if ingredient_id and ingredient_id != 0:
                        ingredient, created = Ingredient.objects.get_or_create(
                            ingredient_id=ingredient_id,
                            defaults={
                                'aisle': ingredient_data.get('aisle',''),
                                'nameClean': ingredient_data.get('nameClean',''),
                                'amount': ingredient_data.get('amount',''),
                                'unit': ingredient_data.get('unit',''),
                            }
                        )
                        recipe.ingredients.add(ingredient)

                # # Ajoutez les ingrédients après avoir sauvegardé l'objet Recipe
                # ingredients_ids = item.get('ingredients_ids', [])
                # ingredients = Ingredient.objects.filter(id__in=ingredients_ids) if ingredients_ids else []
                # recipe.ingredients.set(ingredients)

                # Ajoutez les analyzedInstructions après avoir sauvegardé l'objet Recipe
                analyzed_instructions = item.get('analyzedInstructions', [])
                for instruction_data in analyzed_instructions:
                    instruction = AnalyzedInstruction.objects.create(name=instruction_data.get('name', ''))
                    for step_data in instruction_data.get('steps', []):
                        step = Step.objects.create(
                            number=step_data.get('number', 0),
                            step=step_data.get('step', ''),
                            length_number=step_data.get('length', {}).get('number', None),
                            length_unit=step_data.get('length', {}).get('unit', None)
                        )

                        for ingredient_data in step_data.get('ingredients', []):
                            ingredient_id = ingredient_data.get('id')
                            if ingredient_id and ingredient_id != 0:
                                ingredient, created = Ingredient.objects.get_or_create(
                                    ingredient_id=ingredient_id,
                                    defaults={
                                        'aisle': ingredient_data.get('aisle',''),
                                        'nameClean': ingredient_data.get('nameClean',''),
                                        'amount': ingredient_data.get('amount', 0),
                                        'unit': ingredient_data.get('unit',''),
                                    }
                                )
                                step.ingredients.add(ingredient)
                            else:
                                self.stdout.write(self.style.WARNING('Ingredient data is missing or has invalid id: {}'.format(ingredient_data)))

                        for equipment_data in step_data.get('equipment', []):
                            equipment_name = equipment_data.get('name')
                            if equipment_name:
                                equipment, created = Equipment.objects.get_or_create(
                                    name=equipment_name,
                                )
                                step.equipment.add(equipment)
                            else:
                                self.stdout.write(self.style.WARNING('Equipment data is missing a name: {}'.format(equipment_data)))

                        instruction.steps.add(step)

                    recipe.analyzedInstructions.add(instruction)

                recipe.save()
                self.stdout.write(self.style.SUCCESS('Recette ajoutée avec succès'))
            except KeyError as e:
                self.stdout.write(self.style.WARNING('Probleme de clé: {}'.format(e)))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Une erreur est survenue: {e}'))
