from rest_framework import serializers
from .models import ContactPage


class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPage
        fields = "__all__"
