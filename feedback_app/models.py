from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


def feedback_preview_path(filename: str) -> str:
    """Функция для создания кастомной папки сохранения изображений"""
    return f'preview/feedback/{filename}'


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='имя')
    lastname = models.CharField(max_length=100, verbose_name='фамилия')
    surname  = models.CharField(max_length=100, verbose_name='отчество', **NULLABLE)
    preview = models.ImageField(upload_to=feedback_preview_path, verbose_name='фотография', **NULLABLE)
    date_create = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    content = models.TextField(null=False, blank=True, db_index=True, verbose_name='содержимое')


    @property
    def content_short(self) -> str:
        if len(self.content) < 40:
            return self.content
        return self.content[:40] + '...'


    def __str__(self):
        return f"{self.name} {self.lastname}"


    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
