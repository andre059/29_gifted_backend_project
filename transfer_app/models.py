from django.db import models

from users.models import User


class Transfer(models.Model):
    """Модель для разовых денежных переводов"""

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_transfers", verbose_name="Отправитель")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_transfers", verbose_name="Получатель")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма перевода")
    currency = models.CharField(max_length=3, verbose_name="Валюта", default='RUB')
    description = models.CharField(max_length=255, blank=True, verbose_name="Описание")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время перевода")
    status = models.CharField(max_length=20, choices=(
        ('pending', 'В ожидании'),
        ('processing', 'В обработке'),
        ('completed', 'Завершен'),
        ('failed', 'Ошибка'),
    ), default='pending', verbose_name="Статус")

    def __str__(self):
        return f"Перевод {self.amount} {self.currency} от {self.sender} к {self.recipient}"

    class Meta:
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"
