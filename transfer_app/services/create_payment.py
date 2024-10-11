import os
import uuid

from yookassa import Configuration, Payment

from ..models import PaymentModel


def create_payment(serialized_data):
    """Создает платеж в ЮКассе и возвращает URL страницы оплаты."""
    value = serialized_data.get('value')  # сумма платежа
    payment_type = serialized_data.get('payment_type')  # тип  платежного  метода
    return_url = serialized_data.get('return_url')  # URL, на которую пользователь будет перенаправлен после оплаты

    # Создайте новую запись Payment
    payment = PaymentModel.objects.create(
        transfer_amount=value,
        is_accepted=False,
        payment_id=uuid.uuid4(),  # Генерируем уникальный ID платежа
    )

    payment = Payment.create({
        'amount': {
            'value': value,
            'currency': 'RUB',
        },
        'payment_method_data': {
            'type': payment_type,
        },
        'confirmation': {
            'type': 'redirect',
            'return_url': return_url,
        },
        'metadata': {
            'payment_id': payment.payment_id,  # уникальный идентификатор платежа
        },
        'capture': True,
        'refundable': False,
        'description': 'Пополнение на ' + str(value),
    })

    return payment.confirmation.confirmation_url
