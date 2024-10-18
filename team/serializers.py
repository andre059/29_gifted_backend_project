from rest_framework import serializers
from .models import Developer, DeveloperImage



class DeveloperImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeveloperImage
        fields = ["id", "link"]


class DeveloperSerializer(serializers.ModelSerializer):
    images = DeveloperImageSerializer(many=True, read_only=True)
    class Meta:
        model = Developer
        fields = '__all__'
