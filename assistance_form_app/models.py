from django.db import models
from config.utils import (
    char_field_validator_letters_and_extra,
    text_field_validation, datetime_field,
    phone_number_field,
    email_field
)


class AssistanceForm(models.Model):
    name = char_field_validator_letters_and_extra("Имя", 100, extra=("-",))
    lastname = char_field_validator_letters_and_extra("Фамилия", 100, extra=("-",))
    content = text_field_validation("Чем хотите помочь",)
    phone = phone_number_field("Номер телефона")
    email = email_field("Электронная почта")
    date_create = datetime_field("Дата создания", auto_now_add=True)

    @property
    def content_short(self) -> str:
        return self.content[:40] + ("..." if len(self.content) > 40 else "")

    def __str__(self):
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name = "Предложение помощи"
        verbose_name_plural = "Предложения помощи"