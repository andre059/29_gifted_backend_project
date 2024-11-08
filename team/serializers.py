from rest_framework import serializers
from config.utils import replace_http_to_https_in_link
from .models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)
    
    class Meta:
        model = Developer
        fields = "__all__"
