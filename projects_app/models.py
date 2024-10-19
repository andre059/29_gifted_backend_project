from django.db import models
from config.utils import (
    char_field_specific_length_without_valid,
    image_field,
    text_field_specific_length,
)


class Project(models.Model):
    name = char_field_specific_length_without_valid("Название проекта", 255)
    content = text_field_specific_length("Описание проекта", 1000)

    @property
    def content_short(self) -> str:
        return self.content[:150] + (
            "..." if len(self.content) > 150 else "",
            )

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
    link = image_field("Изображение")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Изображение: {self.project.name}"
