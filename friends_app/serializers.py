from rest_framework import serializers
from .models import Friend, Company, Volunteer
from config.utils import replace_http_to_https_in_link


class FriendSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)

    class Meta:
        model = Friend
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)
    
    class Meta:
        model = Company
        fields = "__all__"


class VolunteerSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)

    class Meta:
        model = Volunteer
        fields = "__all__"
