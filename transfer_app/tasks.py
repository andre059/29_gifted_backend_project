import os
from datetime import timedelta
from celery import shared_task
from django.core.mail import send_mail

from django.utils import timezone

from transfer_app.models import RecurringPayment
from transfer_app.services.create_payment import create_payment

EMAIL_HOST_USER = os.getenv('GIFTED_29_EMAIL_HOST_USER')
@shared_task
def process_recurring_payments():
    """Обработка akтивных платежей"""
    recurring_payments = RecurringPayment.objects.filter(
        is_active=True,
        next_payment_date__lte=timezone.now()
    )

    for recurring_payment in recurring_payments:
        create_payment_in_yookassa.delay(recurring_payment.id)  # Запуск задачи Celery

        # Обновление даты следующего платежа
        recurring_payment.next_payment_date = timezone.now() + timedelta(
            days=30 if recurring_payment.frequency == 'monthly' else 90 if recurring_payment.frequency == 'quarterly' else 365
        )
        recurring_payment.save()


@shared_task
def create_payment_in_yookassa(recurring_payment_id):
    """Создает платеж в ЮКассе для автоплатежа."""

    recurring_payment = RecurringPayment.objects.get(pk=recurring_payment_id)

    # Создаем платеж в ЮКассе
    payment_url = create_payment({
        'value': recurring_payment.amount,
        'payment_type': '',  # Передаем пустое значение для выбора типа платежа на стороне ЮКассы
    })

    return payment_url


def send_recurring_payment_reminder(recurring_payment):
    """Отправляет уведомление о предстоящем автоплатеже."""

    subject = "Напоминание об автоплатеже"
    message = f"{recurring_payment.payment.name} {recurring_payment.payment.surname}, " \
              f"напоминаем, что {recurring_payment.next_payment_date.strftime('%d.%m.%Y')} " \
              f"состоится автоплатеж на сумму {recurring_payment.amount}."
    from_email = EMAIL_HOST_USER  # Заменить на адрес отправителя письма
    to_email = recurring_payment.payment.email

    send_mail(subject, message, from_email, [to_email])
