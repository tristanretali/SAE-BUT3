from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .serializers import UserSerializer
from rest_framework import status
import os


class UserTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="Test user", password="user", email="user@test.net")
        user2 = User.objects.create_user(username="Test user 2", password="user2", email="user2@test.net")
        user3 = User.objects.create_user(username="user3", password="user3", email="user3@test.net")

    def test_number_user(self):
        users = User.objects.filter(username__startswith="Test")
        self.assertEqual(users.count(), 2)

    def test_create_user(self):
        User.objects.create_user(username="bob", password="bob", email="bob@test.net")
        user = User.objects.get(username="bob")
        self.assertEqual(user.email, "bob@test.net")

    def test_delete_user(self):
        User.objects.filter(username__startswith="Test").delete()  # remove 2 articles from 3
        users = User.objects.all()  # 1 article should be remaining
        self.assertEqual(users.count(), 1)


class RESTUSerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.pascal = User.objects.create_user('pascal', 'pascal@test.com', 'pascal')
        self.client.force_authenticate(user=self.pascal)
        self.user1 = User.objects.create_user(username="Test user", password="user", email="user@test.net")
        self.user2 = User.objects.create_user(username="Test user 2", password="user2", email="user2@test.net")
        self.user3 = User.objects.create_user(username="user3", password="user3", email="user3@test.net")

    def test_list_users(self):
        response = self.client.get('/rest/users/')
        users = User.objects.all().order_by('username')
        serializer_data = UserSerializer(users, many=True).data
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.force_authenticate(user=None)

    def test_get_user(self):
        # get article with id 1
        response = self.client.get("/rest/users/2/")
        serializer_data = UserSerializer(self.user1).data
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.force_authenticate(user=None)

    def test_post_user(self):
        new_data = {'username': 'NouveauUser', 'password': 'NouveauUser', 'email': 'nouveau@test.net'}
        response = self.client.post("/rest/users/", new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.force_authenticate(user=None)

    def test_delete_user(self):
        response = self.client.delete("/rest/users/2/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=self.user1.id)
        self.client.force_authenticate(user=None)




