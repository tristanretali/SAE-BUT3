import json

from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest

from rest_framework import viewsets
from rest_framework.decorators import action
from recipe.models import Recipe

from django.contrib.auth import get_user_model
User = get_user_model()

from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer

    @action(detail=False, methods=['POST'])
    def login(self, request):
        try:
            username = request.data.get('username', None)
            password = request.data.get('password', None)
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                request.session['user_id'] = user.id
                return JsonResponse({
                    'username': user.username,
                    'email': user.email,
                    'isSuperuser': user.is_superuser
                })
            else:
                return JsonResponse({"detail": "Invalid credentials"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"detail": "Invalid JSON"}, status=400)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        if request.method == 'POST':
            try:
                user_id = request.session.get('user_id')
                if user_id:
                    django_logout(request)
                    request.session['user_id'] = None
                    return JsonResponse({"message": "Logout successful"}, status=200)
                else:
                    return JsonResponse({"detail": "User is not logged in"}, status=400)
            except Exception as e:
                return HttpResponse('Error logging out: {}'.format(str(e)), status=500)
        else:
            return HttpResponseBadRequest("Only POST method is supported")

    @action(detail=False, methods=['get'])
    def me(self, request):
        try:
            user_id = request.session.get('user_id')
            if user_id:
                user = get_user_model().objects.get(pk=user_id)
                if user is not None:
                    return JsonResponse({
                        'superUser': user.is_superuser,
                        'username': user.username,
                        'email': user.email,
                    })
                else:
                    return JsonResponse({"detail": "User not found"}, status=404)
            else:
                return JsonResponse({"detail": "User is not logged in"}, status=400)
        except Exception as e:
            return HttpResponse('Error getting current user: {}'.format(str(e)), status=500)

    @action(detail=False, methods=['get'])
    def favorites(self, request, pk=None):
        try:
            user_id = request.session.get('user_id')
            if user_id:
                user = get_user_model().objects.get(pk=user_id)
                if user is not None:
                    return JsonResponse({
						'recipes': list(user.favorite_recipes.values())
					})
                else:
                    return JsonResponse({"detail": "User not found"}, status=404)
            else:
                return JsonResponse({"detail": "User not authenticated"}, status=401)
        except Exception as e:
            return JsonResponse({"detail": f"Error to show recipes's: {str(e)}"}, status=500)
        
    @action(detail=False, methods=['POST'])
    def add_favorite(self, request, pk=None):
        try:
            user_id = request.session.get('user_id')
            if user_id:
                user = get_user_model().objects.get(pk=user_id)
                if user is not None:
                    recipe_id = request.data.get('recipe_id')
                    recipe = Recipe.objects.get(pk=recipe_id)
                    if (recipe is None):
                        return JsonResponse({"detail": "Recipe not found"}, status=404)
                    if (recipe in user.favorite_recipes.all()):
                        user.favorite_recipes.remove(recipe)
                    else:
                        user.favorite_recipes.add(recipe)
                    return JsonResponse({
						'is_favorite': recipe in user.favorite_recipes.all()
					})
                else:
                    return JsonResponse({"detail": "User not found"}, status=404)
            else:
                return JsonResponse({"detail": "User not authenticated"}, status=401)
        except Exception as e:
            return JsonResponse({"detail": f"Error to add favorite: {str(e)}"}, status=500)