from rest_framework import serializers
from feedback_app.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    """Сериализатор для отзыввов"""
    class Meta:
        model = Feedback
        fields = (
            'id',
            'name', 
            'lastname', 
            'date_create', 
            'content', 
            'preview',
            )