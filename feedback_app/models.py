from django.db import models
from config.utils import (
    charfield_validator_letters_and_extra,
    imagefield,
    textfield_specific_length,
)


class Feedback(models.Model):
    name = charfield_validator_letters_and_extra("Имя", 100, extra=("-",))
    lastname = charfield_validator_letters_and_extra("Фамилия", 100, extra=("-",))
    link = imagefield("Фото", nullable=True)
    content = textfield_specific_length("Текст отзыва", 1000)
    date_create = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, null=True)

    @property
    def content_short(self) -> str:
        return self.content[:40] + ("..." if len(self.content) > 40 else "")

    def __str__(self):
        return f"{self.name} {self.lastname}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
