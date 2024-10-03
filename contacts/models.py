from django.db import models
from django.contrib.postgres.fields import ArrayField

class ContactPage(models.Model):
    address = models.CharField(
        max_length=255, 
        verbose_name='Адрес',
        help_text="Текст, не более 255 символов",
        )
    phones = ArrayField(models.CharField(
        max_length=255, 
        verbose_name='Телефон',
        help_text="Номер телефона",
        ))
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=200,
        help_text="Укажите электронную почту",
        )
    phone_for_media = models.CharField(
        max_length=255, 
        verbose_name='Телефон для СМИ',
        help_text="Телефоны для СМИ",
        default='+7‒962‒836‒86‒48',
        )
    email_for_media = models.EmailField(
        verbose_name='Электронная почта для СМИ',
        max_length=200,
        help_text="Укажите электронную почту для СМИ",
        default='darserdca54@gmail.com',
        )
    def save(self, *args, **kwargs):
        if not self.pk and ContactPage.objects.exists():
            raise ValueError("Нельзя создать более одного экземпляра ContactPage.")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
    