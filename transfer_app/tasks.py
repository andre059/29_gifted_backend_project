from celery import shared_task
from .models import PaymentModel
from yookassa import Payment
from rest_framework.exceptions import APIException


@shared_task
def update_payment_status_task(payment_id):
    try:
        payment_db = PaymentModel.objects.get(payment_id=payment_id)

        payment_yookassa = Payment.find_one(payment_id)
        if not payment_yookassa:
            raise APIException("Платеж не найден", code="payment_not_found")

        payment_status = payment_yookassa.status

        payment_db.status = payment_status
        payment_db.save()

        return payment_db.id
    except PaymentModel.DoesNotExist:
        raise APIException("Платеж не найден", code="payment_not_found")
