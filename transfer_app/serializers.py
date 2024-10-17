from rest_framework import serializers

from transfer_app.models import PaymentModel


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'


class PaymentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = ['name', 'surname', 'phone', 'email', 'transfer_amount', 'payment_frequency', 'type_transfer',
                  'comment']

    def validate(self, data):
        # Проверка наличия всех обязательных полей
        required_fields = ['name', 'surname', 'phone', 'email', 'transfer_amount', 'payment_frequency',
                           'type_transfer']
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError(f"Обязательное поле '{field}' отсутствует.")

        # Валидация суммы перевода
        transfer_amount_str = str(data['transfer_amount'])
        transfer_amount = float(transfer_amount_str.replace(',', '.'))

        if transfer_amount <= 0:
            raise serializers.ValidationError("Сумма должна быть положительной.")

        return data
