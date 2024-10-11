from rest_framework import serializers

from config.settings import MAX_UPLOAD_SIZE
from .models import Friend, Company, Volunteer
from django.template.defaultfilters import filesizeformat



def check_file(self):
    '''
    Ограничение размера загружаемого файла
    '''
    if self.size > MAX_UPLOAD_SIZE:
        raise serializers.ValidationError(
            f"Пожалуйста, не превышайте размер файла {filesizeformat(MAX_UPLOAD_SIZE)}. Текущий размер файла {filesizeformat(self.size)}"
        )
    return self


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
