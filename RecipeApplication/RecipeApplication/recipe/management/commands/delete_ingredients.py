from django.core.management.base import BaseCommand
from recipe.models import Ingredient

class Command(BaseCommand):
    help = 'Suppirme la liste des ingrédients depuis la base de données'

    def handle(self, *args, **kwargs):
        try:
            ingredients = Ingredient.objects.all().delete()
            
            if ingredients:
                self.stdout.write(self.style.SUCCESS('Ingredient supprimé :'))
            else:
                self.stdout.write(self.style.WARNING('Aucune cuisines trouvé dans la base de données.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Une erreur est survenue : {e}'))
