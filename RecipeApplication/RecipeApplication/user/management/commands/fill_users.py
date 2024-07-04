from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Ajoute des utilisateurs à la base de données'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=int, help='Number of users')
        parser.add_argument('-p', '--password', type=str, help='Password of the users')

    def handle(self, *args, **kwargs):
        fake = Faker()

        for i in range(kwargs['number']):
            username = fake.user_name()
            email = fake.email()
            User.objects.create_user(username=username, email=email, password=kwargs['password'])

        self.stdout.write(self.style.SUCCESS('Ajout des utilisateurs terminé'))
