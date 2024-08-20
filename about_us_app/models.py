from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

def team_member_photo_path(instance: 'TeamMember', filename: str) -> str:
    # Формируем путь для сохранения фото
    return f'photos/TeamMember/{filename}'

class TeamMember(models.Model):
    photo = models.ImageField(upload_to=team_member_photo_path, blank=True, null=True, verbose_name="Фотография")
    name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    role = models.CharField(max_length=100, verbose_name="Роль в проекте")

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"

    def __str__(self):
        return f"{self.name} {self.last_name} - {self.role}"
    
@receiver(post_delete, sender=TeamMember)
def delete_photo_on_delete(sender, instance, **kwargs):
    if instance.photo:
        photo_path = instance.photo.path
        # Проверяем, существует ли файл по указанному пути
        if os.path.isfile(photo_path):
            try:
                os.remove(photo_path)
                print(f'Файл {photo_path} успешно удален')
            except Exception as e:
                print(f'Ошибка при удалении файла {photo_path}: {e}')
        else:
            print(f'Файл {photo_path} не найден')