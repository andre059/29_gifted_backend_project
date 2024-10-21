from feedback_app.models import Feedback
from feedback_app.serializers import FeedbackSerializer
from rest_framework import viewsets


class FeedbackAPIView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    http_method_names = [
        "get", "post"
        ]


