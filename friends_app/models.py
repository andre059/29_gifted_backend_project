from django.db import models
from config.utils import (
    charfield_specific_length_without_valid,
    charfield_validator_letters_and_extra,
    imagefield,
    charfield_with_choices,
    textfield_specific_length,
    emailfield,
)

GENDER = {
    "male": "Мужской",
    "female": "Женский",
}


class Abstract(models.Model):
    time_create = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    time_update = models.DateTimeField(verbose_name="Изменено", auto_now=True)
    is_published = models.BooleanField(
        verbose_name="Актуально на сайте",
        default=True,
        help_text="Если уже неактуально, но может понадобиться, снимите флажок",
    )

    class Meta:
        abstract = True


class Friend(Abstract):
    name = charfield_validator_letters_and_extra("Имя", 100, ("-",))
    last_name = charfield_validator_letters_and_extra("Фамилия", 100, ("-",))
    sur_name = charfield_validator_letters_and_extra(
        "Отчество", 100, (" ",), nullable=True
    )
    gender = charfield_with_choices("Категория", GENDER)
    description = textfield_specific_length("Роль в проекте", 70)
    link = imagefield("Фото", nullable=True)

    class Meta:
        verbose_name = "Человека"
        verbose_name_plural = "Люди"

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Company(Abstract):
    name = charfield_specific_length_without_valid("Название", 255)
    link = imagefield("Логотип", nullable=True)
    description = textfield_specific_length("Чем была полезна:", 85)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"{self.name}"


class Volunteer(models.Model):
    name = charfield_validator_letters_and_extra("Имя", 100, ("-",))
    last_name = charfield_validator_letters_and_extra("Фамилия", 100, ("-",))
    email = emailfield("")
    link = imagefield("Фото", nullable=True)
    is_accept = models.BooleanField(
        verbose_name="Принято пользовательское соглашение",
        default=True,
    )

    class Meta:
        verbose_name = "Волонтер"
        verbose_name_plural = "Волонтеры"

    def __str__(self):
        return f"{self.name}"
