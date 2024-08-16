from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            username='Admin',
            email='admin@gmail.com',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        user.set_password('zxc123qwe789')
        user.save()
