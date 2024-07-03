import json

from django.contrib.auth import login as django_login, logout as django_logout, authenticate, get_user
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer


@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            User.objects.create_user(
                json_data['username'],
                json_data['email'],
                json_data['password'],
            )
            return HttpResponse('OK')
        except json.JSONDecodeError:
            return HttpResponse('Internal Server Error', status=400)
    else:
        return HttpResponseBadRequest("Only POST method is supported")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            user = authenticate(username=json_data['username'], password=json_data['password'])
            if user is not None:
                django_login(request, user)
                request.session['user_id'] = user.id
                return JsonResponse({
                    'username': user.username,
                    'email': user.email,
                })
            else:
                return JsonResponse({"detail": "Invalid credentials"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"detail": "Invalid JSON"}, status=400)
    else:
        return HttpResponseBadRequest("Only POST method is supported")


@csrf_exempt
def logout(request):
    if request.method == 'POST':
        try:
            user_id = request.session.get('user_id')
            if user_id:
                django_logout(request)
                return JsonResponse({"message":"Logout successful"}, status=200)
            else:
                return JsonResponse({"detail": "User is not logged in"}, status=400)
        except Exception as e:
            return HttpResponse('Error logging out: {}'.format(str(e)), status=500)
    else:
        return HttpResponseBadRequest("Only POST method is supported")


@csrf_exempt
def me(request):
    if request.method == 'GET':
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
    else:
        return HttpResponseBadRequest("Only GET method is supported")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
