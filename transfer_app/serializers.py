from rest_framework import serializers

from transfer_app.models import PaymentModel


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = '__all__'


class PaymentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = ['name', 'surname', 'phone', 'email', 'transfer_amount', 'comment']

    def validate(self, data):
        # Проверка наличия всех обязательных полей
        required_fields = ['name', 'surname', 'phone', 'email', 'transfer_amount', 'comment']
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError(f"Обязательное поле '{field}' отсутствует.")

        # Валидация суммы перевода
        transfer_amount = data['transfer_amount']
        if transfer_amount <= 0:
            raise serializers.ValidationError("Сумма должна быть положительной.")
        if transfer_amount > 1000000:
            raise serializers.ValidationError("Превышено максимально допустимое количество")

        return data
