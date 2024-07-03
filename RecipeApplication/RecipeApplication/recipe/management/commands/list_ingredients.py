from django.core.management.base import BaseCommand
from recipe.models import Ingredient

class Command(BaseCommand):
    help = 'Affiche la liste des ingrédients depuis la base de données'

    def handle(self, *args, **kwargs):
        try:
            ingredients = Ingredient.objects.all()

            if ingredients:
                self.stdout.write(self.style.SUCCESS('Liste des ingrédients :'))
                for ingredient in ingredients:
                    self.stdout.write(f'ID: {ingredient.ingredient_id}, Aisle: {ingredient.aisle}, Image: {ingredient.image}, '
                                      f'NameClean: {ingredient.nameClean}, Amount: {ingredient.amount} {ingredient.unit}')
            else:
                self.stdout.write(self.style.WARNING('Aucun ingrédient trouvé dans la base de données.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Une erreur est survenue : {e}'))
