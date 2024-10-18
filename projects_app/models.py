from django.db import models
from config.utils import (
    charfield_specific_length_without_valid,
    imagefield,
    textfield_specific_length,
)


class Project(models.Model):
    name = charfield_specific_length_without_valid("Название проекта", 255)
    content = textfield_specific_length("Описание проекта", 1000)

    @property
    def content_short(self) -> str:
        return self.content[:150] + ("..." if len(self.content) > 150 else "")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="images",
        on_delete=models.CASCADE,
        verbose_name="Проект",
    )
    link = imagefield("Изображение")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Изображение: {self.project.name}"
