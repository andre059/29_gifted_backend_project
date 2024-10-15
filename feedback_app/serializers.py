from rest_framework import serializers
from config.settings import MAX_UPLOAD_SIZE
from feedback_app.models import Feedback
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


class FeedbackSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для отзыввов
    '''
    preview = serializers.FileField(validators=[check_file])

    class Meta:
        model = Feedback
        fields = "__all__"
