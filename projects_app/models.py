import shutil
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.db import models

NULLABLE = {'blank': True, 'null': True}


def docs_path(instance, filename: str) -> str:
    """
    Создает путь для сохранения медиафайла в папке media в виде:
    /имя_приложения/класс/имя_файла
    """
    return (
        f"{__name__.split('.', maxsplit=1)[0]}/{instance.__class__.__name__}/{filename}"
    )


class Project(models.Model):
    name = models.CharField(
        max_length=300,  # думаю, имя не должно быть длиннее
        verbose_name="Наименование проекта",
        help_text="Только буквы не более 300 символов")
    content = models.TextField(
        null=False, 
        blank=True, 
        db_index=True, 
        verbose_name="содержимое",
        max_length=1000,
        help_text="Только буквы не более 1000 символов",
        )


    @property
    def content_short(self) -> str:
        if len(self.content) < 150:
            return self.content
        return self.content[:150] + '...'


    def __str__(self):
        return f"{self.name}"


    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, 
        related_name='images', 
        on_delete=models.CASCADE, 
        verbose_name="Проект",
        )
    image = models.ImageField(
        upload_to=docs_path, 
        verbose_name="Изображение",
        )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Изображение: {self.project.name}"

@receiver(post_delete, sender=Project)
@receiver(post_delete, sender=ProjectImage)
def delete_media_on_delete(sender, instance, **kwargs):
    if isinstance(instance, Project):
        # Если удаляется проект, удаляем всю папку с медиафайлами
        folder_path = os.path.join('media', f'projects/{instance.id}')
        if os.path.exists(folder_path):
            try:
                shutil.rmtree(folder_path)
            except Exception as e:
                print(f"Error removing {folder_path}: {e}")
    elif isinstance(instance, ProjectImage):
        if instance.image:
            image_path = instance.image.path
            try:
                os.remove(image_path)
            except FileNotFoundError:
                pass