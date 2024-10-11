from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class ContactPage(models.Model):
    address = models.CharField(
        max_length=255, 
        verbose_name='Адрес',
        help_text="Текст, не более 255 символов",
        )
    phone_1 = PhoneNumberField(
        blank=True, 
        region='RU', 
        verbose_name='Телефон', 
        help_text="Первый номер телефона",
        )
    phone_2 = PhoneNumberField(
        blank=True, 
        region='RU', 
        verbose_name='Телефон', 
        help_text="Второй номер телефона", 
        null=True,
        )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=200,
        help_text="Укажите электронную почту",
        )
    phone_for_media = PhoneNumberField(
        blank=True, 
        region='RU', 
        verbose_name='Телефон для СМИ', 
        help_text="Телефон для СМИ",
        )
    email_for_media = models.EmailField(
        verbose_name='Электронная почта для СМИ',
        max_length=200,
        help_text="Укажите электронную почту для СМИ",
        default='darserdca54@gmail.com',
        )
    def save(self, *args, **kwargs):
        if not self.pk and ContactPage.objects.exists():
            return
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
    