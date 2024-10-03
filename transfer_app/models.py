import uuid
from decimal import Decimal

from django.core.validators import MaxLengthValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models, transaction as tr

from django.conf import settings
from yookassa import Payment


def is_amount_positive(method):
    """Проверяет положительность суммы"""

    def wrapper(cls, args, kwargs):
        amount = kwargs['amount']
        if amount < 0:
            raise ValueError('Should be positive value')
        return method(cls, args, kwargs)
    return wrapper


class PaymentModel(models.Model):
    """Модель для разовых денежных переводов"""

    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    telephone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Электронная почта")
    transfer_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма перевода")
    type_transfer = models.CharField(max_length=20, verbose_name="Тип перевода", choices=(
        ('using your phone', 'С помощью телефона'),
        ('by map', 'По карте'),
        ('using QR code', 'Через QR код')
    ),
        default='using your phone'
                                     )
    comment = models.TextField(
        blank=True, verbose_name="Комментарий",
        validators=[MaxLengthValidator(255, _("Комментарий не может быть длиннее 255 символов."))])

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    payment_id = models.CharField(max_length=255, unique=True, verbose_name="ID платежа")
    is_accepted = models.BooleanField(default=False) # Перевод принят

    def __str__(self):
        return f"Перевод {self.transfer_amount} от {self.name} {self.surname}"

    class Meta:
        verbose_name = "Разовый перевод"
        verbose_name_plural = "Разовые переводы"

    @is_amount_positive
    def deposit(amount: Decimal) -> Payment:
        """
        Use a classmethod instead of an instance method,
        to acquire the lock we need to tell the database
        to lock it, preventing data update collisions.
        When operating on self the object is already fetched.
        And we don't have  any guaranty that it was locked.
        """

        with tr.atomic():
            payment = PaymentModel.objects.create(
                transfer_amount=amount,
                is_accepted=False,
                payment_id=uuid.uuid4(),  # Генерируем уникальный ID платежа
                name="Имя",  # Добавьте реальное имя
                surname="Фамилия",  # Добавьте реальную фамилию
                telephone="+71234567890",  # Добавьте реальный телефон
                email="test@example.com",  # Добавьте реальный email
                type_transfer='using your phone',  # Добавьте тип перевода
                comment="Комментарий",  # Добавьте комментарий
            )
            transaction = BalanceChange.objects.create(
                payment=payment,
                amount=amount,
                operation_type=BalanceChange.OperationType.DEPOSIT,
            )
            payment.is_accepted = True
            payment.save()
        return transaction


class BalanceChange(models.Model):
    class OperationType(models.TextChoices):
        """Указание типа операции"""

        WITHDRAW = ('WD', 'WITHDRAW')
        DEPOSIT = ('DT', 'DEPOSIT')

    payment = models.ForeignKey(PaymentModel, on_delete=models.PROTECT, related_name='transactions')
    amount = models.DecimalField(
        max_digits=settings.MAX_BALANCE_DIGITS,
        validators=[MinValueValidator(0, message='Should be positive value')],
        decimal_places=2,
        editable=False,
    )
    date_time_creation = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )
    is_accepted = models.BooleanField(default=False)
    operation_type = models.CharField(max_length=20, choices=OperationType.choices)

    def __str__(self) -> str:
        return (
            f'Payment id:  {self.payment} '
            f'Date time of creation: {self.date_time_creation}'
            f'Amount: {self.amount}'
        )

    class Meta:
        ordering = ['-date_time_creation']


class RecurringPayment(models.Model):
    """Модель для регулярных платежей"""

    payment = models.ForeignKey(
        PaymentModel, on_delete=models.PROTECT, related_name='recurring_payments', verbose_name="Платеж"
    )

    amount = models.DecimalField(
        max_digits=settings.MAX_BALANCE_DIGITS,
        validators=[MinValueValidator(0, message='Should be positive value')],
        decimal_places=2,
        verbose_name="Сумма"
    )
    frequency = models.CharField(max_length=20, choices=(
        ('monthly', 'Ежемесячно'),
        ('quarterly', 'Ежеквартально'),
        ('yearly', 'Ежегодно'),
    ), default='monthly', verbose_name="Периодичность")
    next_payment_date = models.DateTimeField(verbose_name="Дата следующего платежа")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f"Автоплатеж {self.amount} {self.frequency} для {self.payment}"

    class Meta:
        verbose_name = "Авто перевод"
        verbose_name_plural = "Авто переводы"
