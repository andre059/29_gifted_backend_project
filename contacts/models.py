from django.db import models

from .validators import validate_phone

class ContactPage(models.Model):
    address = models.CharField(
        max_length=255, 
        verbose_name='Адрес',
        help_text="Текст, не более 255 символов",
        )
    phone_1 = models.CharField(
        max_length=20, 
        verbose_name='Телефон',
        validators=[
            validate_phone,
        ],
        help_text="Первый номер телефона",
        default='+79628368648',
        )
    phone_2 = models.CharField(
        max_length=20, 
        verbose_name='Телефон',
        validators=[
            validate_phone,
        ],
        help_text="Второй номер телефона",
        default='+79628368648',
        )
    email = models.EmailField(
        verbose_name='Электронная почта',
        max_length=200,
        help_text="Укажите электронную почту",
        )
    phone_for_media = models.CharField(
        max_length=20, 
        verbose_name='Телефон для СМИ',
        validators=[
            validate_phone,
        ],
        help_text="Телефоны для СМИ",
        default='+79628368648',
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
    