# import rollbar
# from django.core.exceptions import ObjectDoesNotExist
#
# from ..models import PaymentModel
#
#
# def payment_acceptance(response):
#     """Обрабатывает ответ от ЮКассы и обновляет состояние платежа."""
#     try:
#         payment = PaymentModel.objects.get(payment_id=response['object']['metadata']['payment_id'])
#     except ObjectDoesNotExist:
#         payment_id = response['object']['id']
#         rollbar.report_message(
#             f"Can't get payment for payment id {payment_id}",
#             'warning',
#         )
#         return False
#
#     if response['event'] == 'payment.succeeded':
#         payment.is_accepted = True
#         payment.save()
#     elif response['event'] == 'payment.canceled':
#         payment.is_accepted = False
#         payment.save()
#
#     return True
