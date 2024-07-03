from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_remove_ingredient_recipe_recipepage_ingredients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipePage',
            new_name='Recipe',
        ),
    ]
