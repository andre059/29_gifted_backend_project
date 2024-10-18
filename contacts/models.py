from django.db import models
from config.utils import (
    charfield_specific_length_without_valid,
    emailfield,
    phonenumberfield,
)


class ContactPage(models.Model):
    address = charfield_specific_length_without_valid("Адрес", 255)
    phone_1 = phonenumberfield("Первый номер телефона")
    phone_2 = phonenumberfield("Второй номер телефона", nullable=True)
    email = emailfield("")
    phone_for_media = phonenumberfield("Телефон для СМИ")
    email_for_media = emailfield(" для СМИ")

    def save(self, *args, **kwargs):
        if not self.pk and ContactPage.objects.exists():
            return
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"
