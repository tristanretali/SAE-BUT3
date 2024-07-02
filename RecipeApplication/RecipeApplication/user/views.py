import json

from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

from django.contrib.auth.models import User
from rest_framework import generics, status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
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


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]
