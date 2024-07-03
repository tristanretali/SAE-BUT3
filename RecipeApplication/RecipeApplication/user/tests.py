from django.test import TestCase
from django.contrib.auth.models import User


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