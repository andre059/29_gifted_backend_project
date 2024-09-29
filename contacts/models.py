from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

def docs_path(instance, filename: str) -> str:
    """
    Создает путь для сохранения медиафайла в папке media в виде:
    /имя_приложения/класс/имя_файла
    """
    return (
        f"{__name__.split('.', maxsplit=1)[0]}/{instance.__class__.__name__}/{filename}"
    )


class ContactPage(models.Model):
    header = models.CharField(max_length=200, verbose_name='Заголовок')
    photo = models.ImageField(upload_to=docs_path, verbose_name='Фото')
    short_description = models.TextField(verbose_name='Краткое описание')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phones = models.CharField(max_length=255, verbose_name='Телефоны')
    email = models.EmailField(verbose_name='Электронная почта')
    for_media = models.CharField(max_length=255, verbose_name='Для СМИ')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

@receiver(post_delete, sender=ContactPage)
def delete_mediafile_on_delete(sender, instance, **kwargs):
    """
    Удаляет медиафайл из папки при удалении записи в БД
    """
    if instance.photo:
        photo_path = instance.photo.path
        if os.path.isfile(photo_path):
            try:
                os.remove(photo_path)
                print(f"Файл {photo_path} успешно удален")
            except Exception as e:
                print(f"Ошибка при удалении файла {photo_path}: {e}")
        else:
            print(f"Файл {photo_path} не найден")
