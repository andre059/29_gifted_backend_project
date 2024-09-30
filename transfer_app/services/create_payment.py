import os

from yookassa import Configuration, Payment

from ..models import BalanceChange

Configuration.account_id = os.getenv('GIFTED_29_ACCOUNT_ID')
Configuration.secret_key = os.getenv('GIFTED_29_SHOP_SECRET_KEY')


def create_payment(serialized_data):
    """Создает платеж в ЮКассе и возвращает URL страницы оплаты."""

    value = serialized_data.get('value')  # сумма платежа
    commission = serialized_data.get('commission')  # комиссия, которая учитывается при расчете итоговой суммы
    payment_type = serialized_data.get('payment_type')  # тип  платежного  метода
    return_url = serialized_data.get('return_url')  # URL, на которую пользователь будет перенаправлен после оплаты
    value_with_commission = value * (1 / (1 - commission / 100))  # сумма с учетом комиссии

    change = BalanceChange.objects.create(
        amount=value,
        is_accepted=False,
        operation_type='DEPOSIT',
    )

    payment = Payment.create({
        'amount': {
            'value': value_with_commission,
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
            'payment_id': change.id,  # уникальный идентификатор платежа
        },
        'capture': True,
        'refundable': False,
        'description': 'Пополнение на ' + str(value),
    })

    return payment.confirmation.confirmation_url
