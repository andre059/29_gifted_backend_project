from django.db import models
from config.utils import (
    char_field_specific_length_without_valid,
    email_field,
    phone_number_field,
)


class ContactPage(models.Model):
    address = char_field_specific_length_without_valid("Адрес", 255)
    phone_1 = phone_number_field("Первый номер телефона")
    phone_2 = phone_number_field("Второй номер телефона", nullable=True)
    email = email_field("")
    phone_for_media = phone_number_field("Телефон для СМИ")
    email_for_media = email_field(" для СМИ")

    def save(self, *args, **kwargs):
        if not self.pk and ContactPage.objects.exists():
            return
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
