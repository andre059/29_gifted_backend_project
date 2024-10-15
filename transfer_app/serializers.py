from rest_framework import serializers

from transfer_app.models import PaymentModel


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'


class PaymentFormSerializer(serializers.Serializer):
    class Meta:
        model = PaymentModel
        fields = ['name', 'surname', 'telephone', 'email', 'transfer_amount', 'payment_frequency', 'type_transfer',
                  'comment']

# class CreatePaymentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PaymentModel
#         fields = '__all__'
#
#
# class CreateRecurringPaymentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RecurringPayment
#         fields = '__all__'
