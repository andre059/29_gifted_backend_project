from rest_framework import serializers
from .models import Friend, Company, Volunteer
from config.utils import check_file


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class VolunteerSerializer(serializers.ModelSerializer):
    link = serializers.FileField(validators=[check_file])

    class Meta:
        model = Volunteer
        fields = "__all__"
