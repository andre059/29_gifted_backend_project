from phonenumber_field.phonenumber import to_python
from rest_framework import serializers

def fix_phone(value):
        phone_number = to_python(value)

        if phone_number is None:
            raise serializers.ValidationError("Телефонный номер не может быть пустым.")

        if not phone_number.is_valid():
            raise serializers.ValidationError("Некорректный номер телефона.")

        return phone_number.as_e164