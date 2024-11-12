from django.urls import path, include
from rest_framework.routers import DefaultRouter
from about_us_app.apps import AboutUsAppConfig
from .views import (
    TeamMemberViewSet,
    DocumentViewSet,
    OrganizationDetailViewSet,
    CombinedDataView,
    UserAgreementViewSet
)

app_name = AboutUsAppConfig.name
router = DefaultRouter()

router.register(r"team", TeamMemberViewSet)
router.register(r"doc", DocumentViewSet)
router.register(r"org", OrganizationDetailViewSet)
router.register(r"agreement", UserAgreementViewSet)

urlpatterns = [
    path("separate/", include(router.urls)),
    path("", CombinedDataView.as_view(), name="combined-data"),
]
