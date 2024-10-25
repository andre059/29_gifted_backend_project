from yookassa import Payment
from config.settings import SITE_URL
from django.core.exceptions import ValidationError
from .tasks import update_payment_status_task
from datetime import datetime, timedelta


def create_payment(amount: int, description: str):
    expires_at = (datetime.now() + timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    payment_data = {
        "amount": {
            "value": amount,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": f"https://{SITE_URL}"
        },
        "capture": True,
        "description": description,
        "expires_at": expires_at,
    }
    payment = Payment.create(payment_data)
    return payment


def set_payment_status(request):
    payment_id = request.data.get("payment_id")

    if not payment_id:
        raise ValidationError("Требуется идентификатор платежа")
    task = update_payment_status_task.apply_async((payment_id,), countdown=600)

    return {"message": "Задача обновления статуса запущена, обновится через 10 минут", "task_id": task.id}
