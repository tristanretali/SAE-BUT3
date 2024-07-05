from django.core.management.base import BaseCommand
from recipe.models import Cuisine


class Command(BaseCommand):
    help = 'Ajoute un ingrédient à la base de données'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--name', type=str, help='nom de l\'ingrédient')

    def handle(self, *args, **kwargs):
        try:
            name = kwargs['name']

            Cuisine.objects.create(
                name=name,
            )

            self.stdout.write(self.style.SUCCESS('Ingrédient ajouté avec succès'))
        except KeyError:
            self.stdout.write(self.style.WARNING(
                'Utilisation: python manage.py add_ingredient -id <ingredient_id> -a <aisle> -im <image> -n <nameClean> -am <amount> -u <unit>'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Une erreur est survenue: {e}'))
