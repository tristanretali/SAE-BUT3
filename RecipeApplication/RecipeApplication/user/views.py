import json

from django.contrib.auth import login as django_login, logout as django_logout
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
            User.objects.create(username=json_data['username'], password=json_data['password'],
                                email=json_data['email'])
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
            user = User.objects.get(username=json_data['username'], password=json_data['password'])
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
                return HttpResponse('Logout successful')
            else:
                return JsonResponse({"detail": "User is not logged in"}, status=400)
        except Exception as e:
            return HttpResponse('Error logging out: {}'.format(str(e)), status=500)
    else:
        return HttpResponseBadRequest("Only POST method is supported")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
