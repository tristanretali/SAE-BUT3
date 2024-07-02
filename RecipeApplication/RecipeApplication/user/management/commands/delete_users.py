from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Supprime les user de la base de données'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
