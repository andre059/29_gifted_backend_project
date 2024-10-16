from rest_framework import serializers
from config.utils import check_file
from feedback_app.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    preview = serializers.FileField(validators=[check_file])

    class Meta:
        model = Feedback
        fields = "__all__"
