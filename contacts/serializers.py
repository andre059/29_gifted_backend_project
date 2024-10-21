from rest_framework import serializers
from .models import ContactPage
from config.services import fix_phone


class ContactPageSerializer(serializers.ModelSerializer):

    def validate_phone(self, value):
        return fix_phone(value)
    class Meta:
        model = ContactPage
        fields = "__all__"
