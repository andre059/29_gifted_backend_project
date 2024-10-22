import shutil
from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from config.utils import (
    datetime_field,
    delete_mediafile_on_delete,
    char_field_specific_length_without_valid,
    image_field,
    text_field_specific_length,
    url_field
)


class News(models.Model):
    created_at = created_at = datetime_field(
        name="Дата создания",
        auto_now_add=True
    )

    title = char_field_specific_length_without_valid(
        name="Заголовок",
        number=255
    )
    content = text_field_specific_length(
        name="Содержание",
        number=1000,
    )
    video = url_field(
        name="Видео",
        nullable=True
    )

    short_description = text_field_specific_length(
        name="Краткое описание",
        number=1000    
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = [
            "created_at",
            ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.short_description:
            self.short_description = self.content[:50]
        super().save(*args, **kwargs)


class NewsImage(models.Model):
    news = models.ForeignKey(
        News,
        related_name="images",
        on_delete=models.CASCADE,
        verbose_name="Новость",
    )
    link = image_field("Изображение", nullable=True) 

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Изображение: {self.news.title}"
    