from django.core.management.base import BaseCommand
from recipe.models import Recipe, Ingredient
from wagtail.blocks import StreamValue

class Command(BaseCommand):
    help = 'Ajoute une recette à la base de données'

    def add_arguments(self, parser):
        parser.add_argument('-t', '--title', type=str, required=True, help='Titre de la recette')
        parser.add_argument('-vege', '--vegetarian',type=bool, help='La recette est végétarienne')
        parser.add_argument('-vg', '--vegan',type=bool,  help='La recette est végétalienne')
        parser.add_argument('-ch', '--cheap', type=bool, help='La recette est bon marché')
        parser.add_argument('-hs', '--healthScore', type=int, default=0, help='Score santé de la recette')
        parser.add_argument('-rim', '--readyInMinutes', type=int, help='Temps de préparation en minutes')
        parser.add_argument('-s', '--servings', type=int, help='Nombre de portions')
        parser.add_argument('-i', '--image', type=str, help='Image de la recette')
        parser.add_argument('-ing', '--ingredients', type=int, nargs='+', help='IDs des ingrédients')
        parser.add_argument('-sm', '--summary', type=str, help='Résumé de la recette')
        parser.add_argument('-cu', '--cuisines', type=str, nargs='+', help='Cuisines de la recette')
        parser.add_argument('-ins', '--instructions', type=str, help='Instructions de la recette')
        parser.add_argument('-ai', '--analyzedInstructions', type=str, nargs='+', help='Instructions analysées de la recette')

    def handle(self, *args, **kwargs):
        try:
            title = kwargs['title']
            vegetarian = kwargs['vegetarian']
            vegan = kwargs['vegan']
            cheap = kwargs['cheap']
            healthScore = kwargs['healthScore']
            readyInMinutes = kwargs['readyInMinutes']
            servings = kwargs['servings']
            image = kwargs['image']
            ingredients_ids = kwargs['ingredients']
            summary = kwargs['summary']
            cuisines = kwargs['cuisines']
            instructions = kwargs['instructions']
            analyzedInstructions = kwargs['analyzedInstructions']

            ingredients = Ingredient.objects.filter(id__in=ingredients_ids) if ingredients_ids else []

            recipe = Recipe.objects.create(
                title=title,
                vegetarian=vegetarian,
                vegan=vegan,
                cheap=cheap,
                healthScore=healthScore,
                readyInMinutes=readyInMinutes,
                servings=servings,
                image=image,
                summary=summary,
                instructions=instructions
            )

            if cuisines:
                recipe.cuisines = StreamValue(recipe.cuisines.stream_block, [
                    {'type': 'cuisine', 'value': cuisine} for cuisine in cuisines
                ])

            if analyzedInstructions:
                analyzed_instructions_value = [
                    {
                        'type': 'instruction',
                        'value': {
                            'name': ins.split(':')[0],
                            'steps': [
                                {'number': idx + 1, 'step': step}
                                for idx, step in enumerate(ins.split(':')[1].split(';'))
                            ]
                        }
                    }
                    for ins in analyzedInstructions
                ]
                recipe.analyzedInstructions = StreamValue(
                    recipe.analyzedInstructions.stream_block, analyzed_instructions_value
                )

            recipe.save()
            recipe.ingredients.set(ingredients)

            self.stdout.write(self.style.SUCCESS('Recette ajoutée avec succès'))
        except KeyError:
            self.stdout.write(self.style.WARNING('Utilisation: python manage.py add_recipe -t <title> [-v] [-vg] [-c] [-hs <healthScore>] [-r <readyInMinutes>] [-s <servings>] [-i <image>] [-ing <ingredients>] [-sm <summary>] [-cu <cuisines>] [-ins <instructions>] [-ai <analyzedInstructions>]'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Une erreur est survenue: {e}'))
