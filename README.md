# README

## Introduction

Ce projet est un site web qui permet de trouver des recettes à cuisiner. Les utilisateurs peuvent rechercher des recettes en fonction des ingrédients qu'ils ont. Il comprend plusieurs fonctionnalités et commandes pour la gestion des utilisateurs et des recettes via une interface web et l'interface Wagtail. Il inclut également des commandes spécifiques pour interagir avec une API externe (Spoonacular) et des tests unitaires.

## Fonctionnalités

### Interface Web

- **Création de compte utilisateur** : Les utilisateurs peuvent créer un compte via l'interface web.
- **Authentification utilisateur** : Les utilisateurs peuvent se connecter via l'interface web.
- **Recherche de recette** : Les utilisateurs peuvent rechercher des recettes via l'interface web.
- **Gestion des recettes favorites** : Les utilisateurs peuvent ajouter ou supprimer des recettes de leurs favoris via l'interface web.

### Interface Wagtail

- **Création** : Les administrateurs peuvent créer des recettes et des utilisateurs via l'interface Wagtail.
- **Modification** : Les administrateurs peuvent modifier les recettes et les utilisateurs via l'interface Wagtail.
- **Suppression** : Les administrateurs peuvent supprimer les recettes et les utilisateurs via l'interface Wagtail.
- **Affichage** : Les administrateurs peuvent afficher les recettes et les utilisateurs via l'interface Wagtail.
- **Hooks** : Il y 3 hooks : 
  - `after_create_snippet` : Redirige l'utilisateur vers le site web après la création d'une recette.
  - `register_admin_menu_item` : Permet de rajouter un lien pour retourner sur le site web depuis l'interface Wagtail.
  - `after_create_user` : Assigne un groupe par défaut à un utilisateur après sa création.

## Commandes

- **Ajout de recettes/ingrédients/cuisines via API externe (Spoonacular)** : Commande pour ajouter des recettes, des ingrédients et des cuisines en utilisant l'API Spoonacular.
- **Ajout d'utilisateur** : Commande pour ajouter un utilisateur.
- **Suppression des recettes/ingrédients/utilisateurs/cuisines** : Commande pour supprimer des recettes, des ingrédients, des utilisateurs et des cuisines.
- **Affichage des recettes/ingrédients/utilisateurs/cuisines** : Commande pour afficher des recettes, des ingrédients, des utilisateurs et des cuisines.

## Tests

- **Tests unitaires** : Tests unitaires pour vérifier le bon fonctionnement des fonctionnalités.
- **Tests REST pour les utilisateurs** : Tests pour vérifier les endpoints REST relatifs aux utilisateurs.

Pour lancer les test, se rendre dans le dossier `RecipeApplication/RecipeApplication` et lancer la commande :
```bash
python manage.py test recipe.tests user.tests
```

## Installation

### Front-end

Se rendre dans le dossier `RecipeApplication/RecipeApplication/front-end`, puis lancer la commande :
```bash
npm|bun|pnpm|yarn install
```
<br>

Enfin, pour lancer le front-end, faire :
```bash
npm|bun|pnpm|yarn run dev
```

### Back-end

Se rendre dans le dossier `RecipeApplication/RecipeApplication`, puis lancer la commande :
```bash
pip install -r requirements.txt
```

Suivre le [quickstart Wagtail](https://docs.wagtail.org/en/stable/getting_started/tutorial.html)

Effectuer les migrations