from django.core.management import BaseCommand
from models import Developer  
from django.core.files import File
import os

class Command(BaseCommand):
    help = 'Создание команды разработчиков'

    def handle(self, *args, **options):
        base_dir = 'team_photo/'  
        folders = [
            'Frontend Developer', 
            'Backend Developer', 
            'Backend Team Lead', 
            'Frontend Team Lead', 
            'Project Manager', 
            'Tester',
            ]

        
        for role_dir in folders:
            role_path = os.path.join(base_dir, role_dir)

            
            if not os.path.isdir(role_path):
                self.stdout.write(self.style.ERROR(f'Директория {role_path} не найдена'))
                continue

            
            role = f'{role_dir}'

            
            for filename in os.listdir(role_path): 
                photo_path = os.path.join(role_path, filename)
                file_name = os.path.splitext(filename)[0]  
                try:
                    last_name, first_name, surname = file_name.split(' ')
                except ValueError:
                    self.stdout.write(self.style.ERROR(f'Неверный формат имени файла: {file_name}'))
                    continue

                
                with open(photo_path, 'rb') as f:
                    dev_photo = File(f)
                    developer, created = Developer.objects.get_or_create(
                        first_name=first_name,
                        last_name=last_name,
                        surname=surname,
                        role=role,  
                        defaults={'photo': dev_photo}
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f'{role}: {first_name} {last_name} создан'))
                    else:
                        self.stdout.write(self.style.WARNING(f'{role}: {first_name} {last_name} уже существует'))
