import uuid

from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from events_app.validators import validate_name_or_surname, validate_no_mixed_scripts, \
    validate_number_of_spaces_or_dashes, validate_email, validate_comment


class PaymentModel(models.Model):
    name = models.CharField(
        max_length=64,
        validators=[
            MinLengthValidator(1, _("Имя должно быть не менее 1 символа")),
            MaxLengthValidator(64, _("Имя должно быть не более 64 символов")),
            validate_name_or_surname,
            validate_no_mixed_scripts,
            validate_number_of_spaces_or_dashes,
        ],
        verbose_name="Имя",
    )
    surname = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(1, _("Фамилия должна быть не менее 1 символа")),
            MaxLengthValidator(64, _("Фамилия должна быть не более 64 символов")),
            validate_name_or_surname,
            validate_no_mixed_scripts,
            validate_number_of_spaces_or_dashes
        ],
        verbose_name="Фамилия"
    )
    phone = PhoneNumberField(
        blank=True,
        region='RU',
        verbose_name='Телефон',
    )
    email = models.EmailField(
        validators=[
            MaxLengthValidator(254, _("Email не может быть длиннее 254 символов")),
            validate_email,
        ],
        verbose_name="Электронная почта")
    transfer_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма перевода",
    )
    payment_id = models.CharField(
        max_length=45, unique=True,
        default=uuid.uuid4,
        verbose_name="ID платежа",
    )
    payment_frequency = models.CharField(
        max_length=15,
        choices=[
                ('one-time', 'Разово'),
                ('monthly', 'Ежемесячно')
            ],
    )
    type_transfer = models.CharField(
        max_length=50,
        verbose_name="Тип перевода",
        choices=(
                ('using your phone', 'С помощью телефона'),
                ('by map', 'По карте'),
                ('using QR code', 'Через QR код')
        ),
        default='using your phone',
    )
    comment = models.TextField(
        blank=True,
        verbose_name="Комментарий",
        validators=[
            MaxLengthValidator(200, _("Комментарий не может быть длиннее 200 символов.")),
            validate_no_mixed_scripts,
            validate_number_of_spaces_or_dashes,
            validate_comment,
        ]
    )
    status = models.CharField(
        max_length=20,
        default='pending',
    )
    is_accepted = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )

    def __str__(self):
        return f"Перевод {self.transfer_amount} от {self.name} {self.surname}"

    class Meta:
        verbose_name = _("Платеж")
        verbose_name_plural = _("Платежи")
