from django.urls import path, include
from rest_framework.routers import DefaultRouter
from about_us_app.apps import AboutUsAppConfig
from .views import (
    FriendViewSet,
    CompanyViewSet,
    VolunteerViewSet,
)

app_name = AboutUsAppConfig.name
router = DefaultRouter()

router.register(
    r"people", FriendViewSet,
    )
router.register(
    r"companies", CompanyViewSet,
    )
router.register(
    r"volunteer", VolunteerViewSet,
    )

urlpatterns = [
    path("", include(router.urls)),
]
