import shutil
from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

from news_app.utils import docs_path

class News(models.Model):
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        ) 
    title = models.CharField(
        max_length=300, 
        verbose_name="Заголовок",
        )
    content = models.TextField(
        verbose_name="Содержание",
        )
    video = models.URLField(
        blank=True, 
        null=True, 
        verbose_name="Видео",
        )  
    short_description = models.TextField(
        verbose_name="Краткое описание", 
        blank=True, 
        null=True,
        max_length=1000,
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
    image = models.ImageField(
        upload_to=docs_path, 
        verbose_name="Изображение",
        )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Изображение: {self.news.title}"
    
@receiver(post_delete, sender=News)
@receiver(post_delete, sender=NewsImage)
def delete_media_on_delete(sender, instance, **kwargs):
    if isinstance(instance, News):
        # Если удаляется новость, удаляем всю папку с медиафайлами
        folder_path = os.path.join('media', f'news/{instance.id}')
        if os.path.exists(folder_path):
            try:
                shutil.rmtree(folder_path)
            except Exception as e:
                print(f"Error removing {folder_path}: {e}")
    elif isinstance(instance, NewsImage):
        if instance.image:
            image_path = instance.image.path
            try:
                os.remove(image_path)
            except FileNotFoundError:
                pass