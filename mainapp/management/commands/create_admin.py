from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
from userapp.models import MyUser
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Create superuser'

    def handle(self, *args, **options):
        try:
            user = MyUser.objects.create_superuser(
                username='admin',
                email='<EMAIL>',
                password='12345'
            )



        except IntegrityError:
            raise CommandError('A user with that username already')
        else:
            self.stdout.write(self.style.SUCCESS('superuser created!'))


