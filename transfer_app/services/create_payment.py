# import os
# import uuid
#
# from yookassa import Configuration, Payment
#
# from ..models import PaymentModel
#
#
# Configuration.account_id = os.environ.get('GIFTED_29_ACCOUNT_ID')
# Configuration.secret_key = os.environ.get('GIFTED_29_SHOP_SECRET_KEY')
#
#
# def create_payment(serialized_data):
#     """Создает платеж в ЮКассе и возвращает URL страницы оплаты."""
#     transfer_amount = serialized_data.get('transfer_amount')  # сумма платежа
#     payment_type = serialized_data.get('type_transfer')  # тип  платежного  метода
#     return_url = serialized_data.get('return_url')  # URL, на которую пользователь будет перенаправлен после оплаты
#
#     # Проверка наличия необходимых данных
#     # if not transfer_amount or not payment_type or not return_url:
#     #     raise ValueError("Недостаточно данных для создания платежа")
#
#     # Создаем новую запись Payment
#     payment = PaymentModel.objects.create(
#         transfer_amount=transfer_amount,
#         is_accepted=False,
#         payment_id=uuid.uuid4(),  # Генерируем уникальный ID платежа
#     )
#
#     # Настройка подключения к API YooKassa
#     if not Configuration.account_id or not Configuration.secret_key:
#         raise ValueError("Учетные данные для YooKassa не установлены")
#
#     payment = Payment.create({
#         'amount': {
#             'value': transfer_amount,
#             'currency': 'RUB',
#         },
#         'payment_method_data': {
#             'type': payment_type,
#         },
#         'confirmation': {
#             'type': 'redirect',
#             'return_url': return_url,
#         },
#         'metadata': {
#             'payment_id': str(payment.payment_id),  # уникальный идентификатор платежа
#         },
#         'capture': True,
#         'refundable': False,
#         'description': 'Пополнение на ' + str(transfer_amount),
#     })
#
#     return payment.confirmation.confirmation_url
