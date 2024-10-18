# models.py
from django.db import models
from config.utils import (
    charfield_specific_length_without_valid,
    charfield_validator_letters_and_extra,
    imagefield)



class Developer(models.Model):
    first_name = charfield_validator_letters_and_extra("Имя", 50, extra=("-",))
    last_name = charfield_validator_letters_and_extra("Фамилия", 50, extra=("-",))
    surname = charfield_validator_letters_and_extra("Отчество", 50, (" ",), nullable=True)
    role = charfield_specific_length_without_valid("Роль в проекте", 100
                                                   )# Например: Backend Developer, Frontend Developer

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'


class DeveloperImage(models.Model):
    developer = models.ForeignKey(
        Developer,
        related_name="images",
        on_delete=models.CASCADE,
        verbose_name="Разработчик",
    )
    link = imagefield("Изображение")

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f"Изображение: {self.developer.first_name} {self.developer.last_name}"
