import json

from django.contrib.auth import login as django_login, logout as django_logout, authenticate, get_user
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.decorators import action

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
                user = get_user(request)
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

    @action(detail=True, methods=['get'])
    def favoris(self, request, pk=None):
        try:
            user_id = request.session.get('user_id')
            if user_id:
                user = get_user(request)
                if user is not None:
                    return JsonResponse({
						'recipes': [recipe for recipe in user.recipes]
					})
                else:
                    return JsonResponse({"detail": "User not found"}, status=404)
            else:
                return JsonResponse({"detail": "User not authenticated"}, status=401)
        except Exception as e:
            return JsonResponse({"detail": f"Error to show recipes's: {str(e)}"}, status=500)
        
    @action(detail=True, methods=['post'])
    def add_favori(self,request, pk=None):
        try:
            user_id = request.session.get('user_id')
            recipe = request.data.get('recipe', None)
            if user_id:
                user = get_user(request)
                if user is not None:
                    if recipe in user.recipes.all():
                        user.recipes.remove(recipe)
                    else:
                        user.recipes.add(recipe)
                    user.save()
                    return JsonResponse({
                        'is_favorite': recipe in user.recipes.all()
                    })
                else:
                    return JsonResponse({"detail": "User not found"}, status=404)
            else:
                return JsonResponse({"detail": "User not authenticated"}, status=401)
        except Exception as e:
            return JsonResponse({"detail": f"Error adding recipe to user's favorites: {str(e)}"}, status=500)