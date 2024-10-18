from django.urls import path, include
from rest_framework.routers import DefaultRouter
from about_us_app.apps import AboutUsAppConfig
from .views import (
    TeamMemberViewSet,
    DocumentViewSet,
    OrganizationDetailViewSet,
    CombinedDataView,
)

app_name = AboutUsAppConfig.name
router = DefaultRouter()

router.register(r"team", TeamMemberViewSet)
router.register(r"doc", DocumentViewSet)
router.register(r"org", OrganizationDetailViewSet)

urlpatterns = [
    path("separate/", include(router.urls)),
    path("", CombinedDataView.as_view(), name="combined-data"),
]
