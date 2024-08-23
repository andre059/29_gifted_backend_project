from feedback_app.models import Feedback
from feedback_app.paginators import FeedbackPaginator
from feedback_app.serializers import FeedbackSerializer
from rest_framework import viewsets


class FeedbackAPIView(viewsets.ModelViewSet):
    """Функция для создания, редактирования и удаления отзывов, а также
        просмотра всего списка отзывов и просмотра отдельного отзыва"""
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    pagination_class = FeedbackPaginator
