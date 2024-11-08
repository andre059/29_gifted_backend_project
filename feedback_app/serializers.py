from rest_framework import serializers
from feedback_app.models import Feedback
from config.utils import replace_http_to_https_in_link


class FeedbackSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)

    class Meta:
        model = Feedback
        fields = "__all__"
