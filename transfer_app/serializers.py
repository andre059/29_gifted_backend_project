from rest_framework import serializers
from transfer_app.models import PaymentModel
from config.services import fix_phone


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentModel
        fields = [
            "name", "last_name", "phone",
            "email", "transfer_amount", "comment",
        ]

    def validate_phone(self, value):
        return fix_phone(value)

    def validate(self, data):

        required_fields = [
            "name", "last_name", "phone",
            "email", "transfer_amount", "comment",
        ]
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError(f"Обязательное поле '{field}' отсутствует.")

        transfer_amount = data["transfer_amount"]
        if transfer_amount <= 0:
            raise serializers.ValidationError("Сумма должна быть больше нуля.")
        if transfer_amount > 1000000:
            raise serializers.ValidationError("Превышено максимально допустимое количество")

        return data
