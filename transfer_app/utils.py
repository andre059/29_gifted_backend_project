from yookassa import Payment

from config.settings import SITE_URL
from django.core.exceptions import ValidationError
from rest_framework.request import Request
from transfer_app.models import PaymentModel
from rest_framework.exceptions import APIException



def create_payment(amount: int, description: str):
    payment_data = {
        "amount": {
            "value": amount,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"http://{SITE_URL}"
        },
        "capture": True,
        "description": description
    }
    payment = Payment.create(payment_data)
    return payment

def set_payment_status(request: Request):
    try:
        payment_id = request.data.get('payment_id')
        if not payment_id:
            raise ValidationError("Требуется идентификатор платежа")

        payment_db = PaymentModel.objects.get(payment_id=payment_id)
        
        payment_yookassa = Payment.find_one(payment_id)
        if not payment_yookassa:
            raise APIException("Платеж не найден", code="payment_not_found")
        
        payment_status = payment_yookassa.status
        
        payment_db.status = payment_status
        payment_db.save()

        return payment_db

    except PaymentModel.DoesNotExist as e:
        raise APIException("Платеж не найден", code="payment_not_found")