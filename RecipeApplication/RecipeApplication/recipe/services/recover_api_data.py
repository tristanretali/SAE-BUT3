import os
from dotenv import load_dotenv
import requests

load_dotenv()
SPOONACULAR_API_KEY = os.environ.get('SPOONACULAR_API_KEY')


def recover_one_hundred_recipes(offset: int) -> list:
    recipes_data = []
    url = f'https://api.spoonacular.com/recipes/complexSearch?apiKey={SPOONACULAR_API_KEY}'
    params = {
        'number': 2,
        'offset': offset
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    for recipe_data in data["results"]:
        recipes_data.append(recover_recipe_details(recipe_data['id']))
    return recipes_data


def recover_recipe_details(recipe_id: int) -> dict:
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={SPOONACULAR_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data


print(recover_one_hundred_recipes(0))
