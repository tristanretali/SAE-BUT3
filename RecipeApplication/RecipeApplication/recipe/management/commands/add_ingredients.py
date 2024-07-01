# management/commands/add_ingredient.py

from django.core.management.base import BaseCommand
from recipe.models import Ingredient

class Command(BaseCommand):
    help = 'Ajoute un ingrédient à la base de données'

    def add_arguments(self, parser):
        parser.add_argument('-id', '--ingredient_id', type=int, help='ID de l\'ingrédient')
        parser.add_argument('-a', '--aisle', type=str, help='Aisle de l\'ingrédient')
        parser.add_argument('-im', '--image', type=str, help='Image de l\'ingrédient')
        parser.add_argument('-n', '--nameClean', type=str, help='Nom propre de l\'ingrédient')
        parser.add_argument('-am', '--amount', type=float, help='Quantité de l\'ingrédient')
        parser.add_argument('-u', '--unit', type=str, help='Unité de mesure de l\'ingrédient')

    def handle(self, *args, **kwargs):
        try:
            ingredient_id = kwargs['ingredient_id']
            aisle = kwargs['aisle']
            image = kwargs['image']
            nameClean = kwargs['nameClean']
            amount = kwargs['amount']
            unit = kwargs['unit']

            Ingredient.objects.create(
                ingredient_id=ingredient_id,
                aisle=aisle,
                image=image,
                nameClean=nameClean,
                amount=amount,
                unit=unit
            )

            self.stdout.write(self.style.SUCCESS('Ingrédient ajouté avec succès'))
        except KeyError:
            self.stdout.write(self.style.WARNING('Utilisation: python manage.py add_ingredient -id <ingredient_id> -a <aisle> -im <image> -n <nameClean> -am <amount> -u <unit>'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Une erreur est survenue: {e}'))