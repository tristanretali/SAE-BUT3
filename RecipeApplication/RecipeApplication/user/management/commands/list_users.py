from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    help = 'Liste les user de la base de données'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            self.stdout.write(self.style.SUCCESS(f'Username: {user.username}, password: {user.password}, email: {user.email}'))
