import rollbar
from django.core.exceptions import ObjectDoesNotExist

from ..models import BalanceChange


def payment_acceptance(response):
    """Обрабатывает ответ от ЮКассы и обновляет состояние платежа."""

    try:
        table = BalanceChange.objects.get(
            id=response['object']['metadata']['payment_id'],
        )
    except ObjectDoesNotExist:
        payment_id = response['object']['id']
        rollbar.report_message(
            f"Can't get table for payment id {payment_id}",
            'warning',
        )
        return False

    if response['event'] == 'payment.succeeded':
        table.is_accepted = True
        table.save()
    elif response['event'] == 'payment.canceled':
        table.delete()

    return True
