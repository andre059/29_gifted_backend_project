# models.py
from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .utils import docs_path
from django.core.validators import RegexValidator


class Developer(models.Model):
    photo = models.ImageField(
        upload_to=docs_path, 
        verbose_name='Фотография',
        )
    first_name = models.CharField(
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я]+$")], 
        max_length=50, 
        verbose_name='Имя',
        )
    last_name = models.CharField(
        validators=[RegexValidator(regex=r"^[a-zA-Zа-яА-Я]+$")],
        max_length=50, 
        verbose_name='Фамилия')
    role = models.CharField(
        max_length=100, 
        verbose_name='Роль в проекте',
        )  # Например: Backend Developer, Frontend Developer

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'

@receiver(post_delete, sender=Developer)
def delete_developer_photo_on_delete(sender, instance, **kwargs):
    
    file_path = instance.photo.path
    
    
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"File {file_path} not found for removal.")
        except Exception as e:
            print(f"Error removing {file_path}: {e}")
