from django.core.management.base import BaseCommand
from recipe.models import Recipe

class Command(BaseCommand):
    help = 'Affiche la liste des ingrédients depuis la base de données'

    def handle(self, *args, **kwargs):
        try:
            cuisines = Recipe.objects.all().delete()
            
            if cuisines:
                self.stdout.write(self.style.SUCCESS('recettes supprimé :'))
            else:
                self.stdout.write(self.style.WARNING('Aucune cuisines trouvé dans la base de données.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Une erreur est survenue : {e}'))
