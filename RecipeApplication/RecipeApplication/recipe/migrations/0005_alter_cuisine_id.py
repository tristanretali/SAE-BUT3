# Generated by Django 5.0.6 on 2024-07-02 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_cuisine_equipment_remove_recipe_analyzedinstructions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuisine',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
