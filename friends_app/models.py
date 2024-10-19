from django.db import models
from config.utils import (
    char_field_specific_length_without_valid,
    char_field_validator_letters_and_extra,
    image_field,
    char_field_with_choices,
    text_field_specific_length,
    email_field, datetime_field, boolean_field
)

GENDER = {
    "male": "Мужской",
    "female": "Женский",
}


class Abstract(models.Model):
    time_create = datetime_field("Создано", auto_now_add=True)
    time_update = datetime_field("Создано", auto_now=True)
    is_published = boolean_field("Актуально на сайте",
        default=True,
        help_text="Если уже неактуально, но может понадобиться, снимите флажок",
    )

    class Meta:
        abstract = True


class Friend(Abstract):
    name = char_field_validator_letters_and_extra("Имя", 100, ("-",))
    last_name = char_field_validator_letters_and_extra("Фамилия", 100, ("-",))
    sur_name = char_field_validator_letters_and_extra(
        "Отчество", 100, (" ",), nullable=True
    )
    gender = char_field_with_choices("Категория", GENDER)
    description = text_field_specific_length("Роль в проекте", 70)
    link = image_field("Фото", nullable=True)

    class Meta:
        verbose_name = "Человека"
        verbose_name_plural = "Люди"

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Company(Abstract):
    name = char_field_specific_length_without_valid("Название", 255)
    link = image_field("Логотип", nullable=True)
    description = text_field_specific_length("Чем была полезна:", 70)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"{self.name}"


class Volunteer(models.Model):
    name = char_field_validator_letters_and_extra("Имя", 100, ("-",))
    last_name = char_field_validator_letters_and_extra("Фамилия", 100, ("-",))
    email = email_field("")
    link = image_field("Фото", nullable=True)
    is_accept = boolean_field("Принято пользовательское соглашение",
        default=True,
    )

    class Meta:
        verbose_name = "Волонтер"
        verbose_name_plural = "Волонтеры"

    def __str__(self):
        return f"{self.name}"
