from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects_app.apps import ProjectsAppConfig
from projects_app.views import ProjectAPIView


app_name = ProjectsAppConfig.name
router = DefaultRouter()
router.register(
    r"", ProjectAPIView,
    )

urlpatterns = [
    path("", include(router.urls)),
]
