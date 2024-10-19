from django.db import models
from config.utils import (
    char_field_validator_letters_and_extra,
    image_field,
    text_field_for_comment, datetime_field
)


class Feedback(models.Model):
    name = char_field_validator_letters_and_extra("Имя", 100, extra=("-",))
    lastname = char_field_validator_letters_and_extra("Фамилия", 100, extra=("-",))
    link = image_field("Фото", nullable=True)
    content = text_field_for_comment("Текст отзыва",)
    date_create = datetime_field("Дата создания", auto_now_add=True)

    @property
    def content_short(self) -> str:
        return self.content[:40] + ("..." if len(self.content) > 40 else "")

    def __str__(self):
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
