from django.urls import path, include
from rest_framework.routers import DefaultRouter
from feedback_app.apps import FeedbackAppConfig
from feedback_app.views import FeedbackAPIView


app_name = FeedbackAppConfig.name
router = DefaultRouter()
router.register(
    r"", FeedbackAPIView,
    )

urlpatterns = [
    path("", include(router.urls)),
]
