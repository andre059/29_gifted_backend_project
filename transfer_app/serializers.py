from rest_framework import serializers

from transfer_app.models import PaymentModel, RecurringPayment


class CreatePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'


class CreateRecurringPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringPayment
        fields = '__all__'
