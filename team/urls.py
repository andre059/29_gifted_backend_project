from django.urls import path, include
from rest_framework.routers import DefaultRouter
from team.apps import TeamConfig
from .views import DeveloperViewSet

app_name = TeamConfig.name
router = DefaultRouter()

router.register(
    r"", DeveloperViewSet,
    )

urlpatterns = [
    path("", include(router.urls)),
]
