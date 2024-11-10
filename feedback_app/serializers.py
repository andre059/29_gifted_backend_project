from rest_framework import serializers
from feedback_app.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link and isinstance(representation.get('link'), str):
            representation['link'] = representation['link'].replace('http://', 'https://')
        return representation

    class Meta:
        model = Feedback
        fields = "__all__"
