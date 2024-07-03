from django.core.management.base import BaseCommand
from recipe.models import Recipe

class Command(BaseCommand):
    help = 'Affiche la liste des recettes depuis la base de données'

    def handle(self, *args, **kwargs):
        try:
            recipes = Recipe.objects.all()

            if recipes:
                self.stdout.write(self.style.SUCCESS('Liste des recettes :'))
                for recipe in recipes:
                    self.stdout.write(f'Title: {recipe.title}, ID: {recipe.id}')
                    self.stdout.write(f'    Vegetarian: {recipe.vegetarian}')
                    self.stdout.write(f'    Vegan: {recipe.vegan}')
                    self.stdout.write(f'    Cheap: {recipe.cheap}')
                    self.stdout.write(f'    Health Score: {recipe.healthScore}')
                    self.stdout.write(f'    Ready in Minutes: {recipe.readyInMinutes}')
                    self.stdout.write(f'    Servings: {recipe.servings}')
                    self.stdout.write(f'    Image: {recipe.image}')
                    self.stdout.write(f'    Ingredients: {", ".join([ingredient.nameClean for ingredient in recipe.ingredients.all()])}')
                    self.stdout.write(f'    Summary: {recipe.summary}')
                    self.stdout.write(f'    Cuisines: {", ".join([cuisine.name for cuisine in recipe.cuisines.all()])}')
                    self.stdout.write(f'    Instructions: {recipe.instructions}')
                    self.stdout.write('    Analyzed Instructions:')
                    for analyzed_instruction in recipe.analyzedInstructions.all():
                        self.stdout.write(f'        {analyzed_instruction.name or "Unnamed Instruction"}:')
                        for step in analyzed_instruction.steps.all():
                            self.stdout.write(f'            Step {step.number}: {step.step}')
                            # ingredient with amount and unit
                            self.stdout.write('                Ingredients:')
                            for ingredient in step.ingredients.all():
                                self.stdout.write(f'                    {ingredient.nameClean}: {ingredient.amount} {ingredient.unit}')
                            # equipment
                            self.stdout.write('                Equipment:')
                            for equipment in step.equipment.all():
                                self.stdout.write(f'                    {equipment.name}')  

            else:
                self.stdout.write(self.style.WARNING('Aucune recette trouvée dans la base de données.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Une erreur est survenue : {e}'))
