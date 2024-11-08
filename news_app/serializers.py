from rest_framework import serializers
from config.utils import replace_http_to_https_in_link
from .models import News, NewsImage

class NewsImageSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)

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

