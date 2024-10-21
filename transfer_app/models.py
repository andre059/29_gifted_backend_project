from django.utils.translation import gettext_lazy as _
from django.db import models
from config.utils import (
    phone_number_field,
    char_field_validator_letters_and_extra,
    decimal_field,
    char_field_with_default,
    char_field_for_payment,
    email_field, text_field_validation, datetime_field
)


class PaymentModel(models.Model):
    name = name = char_field_validator_letters_and_extra("Имя", 100, ("-",))
    last_name = char_field_validator_letters_and_extra("Фамилия", 100, ("-",))
    phone = phone_number_field("Телефон")
    email = email_field("Электронная почта")
    transfer_amount = decimal_field("Сумма перевода",)
    payment_id = char_field_for_payment("ID платежа", 100)
    comment = text_field_validation("Комментарий",)
    status = char_field_with_default(name="Статус платежа", number=20, default="pending",)
    created_at = datetime_field("Дата и время создания", auto_now_add=True,)
    updated_at = datetime_field("Дата и время обновления", auto_now=True,)

    def __str__(self):
        return f"Перевод {self.transfer_amount} от {self.name} {self.last_name}"

    class Meta:
        verbose_name = _("Платеж")
        verbose_name_plural = _("Платежи")
