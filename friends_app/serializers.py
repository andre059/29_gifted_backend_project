from rest_framework import serializers
from .models import Friend, Company, Volunteer


class FriendSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link and isinstance(representation.get('link'), str):
            representation['link'] = representation['link'].replace('http://', 'https://')
        return representation
    
    class Meta:
        model = Friend
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link and isinstance(representation.get('link'), str):
            representation['link'] = representation['link'].replace('http://', 'https://')
        return representation
    
    class Meta:
        model = Company
        fields = "__all__"


class VolunteerSerializer(serializers.ModelSerializer): 
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link and isinstance(representation.get('link'), str):
            representation['link'] = representation['link'].replace('http://', 'https://')
        return representation

    class Meta:
        model = Volunteer
        fields = "__all__"
