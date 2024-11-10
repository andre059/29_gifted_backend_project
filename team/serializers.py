from rest_framework import serializers
from .models import Developer

class DeveloperSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link and isinstance(representation.get('link'), str):
            representation['link'] = representation['link'].replace('http://', 'https://')
        return representation
    
    class Meta:
        model = Developer
        fields = "__all__"
