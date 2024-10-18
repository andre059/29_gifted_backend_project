import shutil
from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from config.utils import (
    datetimefield,
    delete_mediafile_on_delete,
    docs_path,
    charfield_specific_length_without_valid,
    imagefield,
    textfield_specific_length,
    urlfield
)

NULLABLE = {"blank": True, "null": True}

class News(models.Model):
    created_at = created_at = datetimefield(
        name="Дата создания",
        auto_now_add=True
    )

    title = charfield_specific_length_without_valid(
        name="Заголовок",
        number=300
    )
    content = textfield_specific_length(
        name="Содержание",
        number=1300,
    )
    video = urlfield(
        name="Видео",
        nullable=True
    )

    short_description = textfield_specific_length(
        name="Краткое описание",
        number=1000    
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.short_description:
            self.short_description = self.content[:50]
        super().save(*args, **kwargs)


class NewsImage(models.Model):
    news = models.ForeignKey(
        News,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Новость",
    )
    link = imagefield("Изображение", nullable=True) 

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Изображение: {self.news.title}"
    
@receiver(post_delete, sender=News)
@receiver(post_delete, sender=NewsImage)
def delete_media_on_delete(sender, instance, **kwargs):
    if isinstance(instance, News):
        for image in instance.images.all():
            delete_mediafile_on_delete(sender=NewsImage, instance=image, **kwargs)
    elif isinstance(instance, NewsImage):
        delete_mediafile_on_delete(sender=NewsImage, instance=instance, **kwargs)