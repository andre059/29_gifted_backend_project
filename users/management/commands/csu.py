from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            username='Admin',
            defaults={
                'email': 'admin@gmail.com',
                'is_active': True,
                'is_staff': True,
                'is_superuser': True,
            }
        )

        if created:
            user.set_password('zxc123qwe789')
            user.save()
            self.stdout.write('Admin created')
        else:
            self.stdout.write('Admin already exists')
