from rest_framework import serializers

from transfer_app.models import PaymentModel


class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'
