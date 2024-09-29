from django.conf import settings
from django.core.validators import MinValueValidator
from rest_framework import serializers

from transfer_app.models import PaymentModel


class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'


class CreateYooKassaPaymentSerializer(serializers.Serializer):
    """Возвращает данные для создания платежа на YooKassa"""

    value = serializers.DecimalField(
        decimal_places=2,
        max_digits=settings.MAX_BALANCE_DIGITS,
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )
    commission = serializers.DecimalField(
        decimal_places=1,
        max_digits=settings.MAX_BALANCE_DIGITS,
        validators=[MinValueValidator(0, message='Insufficient Funds')],
    )
    payment_type = serializers.CharField(max_length=20)
    return_url = serializers.URLField()
