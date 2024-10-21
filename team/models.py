from django.db import models
from config.utils import (
    char_field_specific_length_without_valid,
    char_field_validator_letters_and_extra,
    image_field)



class Developer(models.Model):
    first_name = char_field_validator_letters_and_extra("Имя", 100, extra=("-",))
    last_name = char_field_validator_letters_and_extra("Фамилия", 100, extra=("-",))
    sur_name = char_field_validator_letters_and_extra("Отчество", 100, (" ",), nullable=True)
    role = char_field_specific_length_without_valid("Роль в проекте", 100)
    link = image_field("Фотография")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Разработчик"
        verbose_name_plural = "Разработчики"
