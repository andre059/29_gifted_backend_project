from django.urls import path, include
from rest_framework.routers import DefaultRouter
from assistance_form_app.apps import AssistanceFormAppConfig
from assistance_form_app.views import AssistanceFormAPIView


app_name = AssistanceFormAppConfig.name
router = DefaultRouter()
router.register(
    r"", AssistanceFormAPIView,
    )

urlpatterns = [
    path("", include(router.urls)),
]
