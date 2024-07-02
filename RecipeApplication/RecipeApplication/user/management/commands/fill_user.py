from django.core.management.base import BaseCommand
from faker import Faker
from user.models import User


class Command(BaseCommand):
    help = 'Ajoute des utilisateurs à la base de données'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--number', type=str, help='Number of users')

    def handle(self, *args, **kwargs):
        fake = Faker()

        for i in range(kwargs['number']):  # Adjust the number of users you want to create
            username = fake.user_name()
            password = fake.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
            email = fake.email()

            User.objects.create_user(username=username, email=email, password=password)

            self.stdout.write(self.style.SUCCESS('Ajout des utilisateurs terminé'))
