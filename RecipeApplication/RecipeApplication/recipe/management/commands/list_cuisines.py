from django.core.management.base import BaseCommand
from recipe.models import Cuisine

class Command(BaseCommand):
    help = 'Affiche la liste des ingrédients depuis la base de données'

    def handle(self, *args, **kwargs):
        try:
            cuisines = Cuisine.objects.all()

            if cuisines:
                self.stdout.write(self.style.SUCCESS('Liste des ingrédients :'))
                for cuisine in cuisines:
                    self.stdout.write(f'NameClean: {cuisine.name},ID: {cuisine.id}')
            else:
                self.stdout.write(self.style.WARNING('Aucune cuisines trouvé dans la base de données.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Une erreur est survenue : {e}'))
