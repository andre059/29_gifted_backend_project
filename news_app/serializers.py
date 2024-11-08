from rest_framework import serializers
from .models import News, NewsImage

class NewsImageSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['link'] = representation['link'].replace('http://', 'https://')
        return representation
    class Meta:
        model = NewsImage
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(
        many=True, read_only=True,
        )

    class Meta:
        model = News
        fields = "__all__"

