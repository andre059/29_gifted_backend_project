from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamMemberViewSet, DocumentViewSet, OrganizationDetailViewSet

router = DefaultRouter()
router.register(r'about-us', TeamMemberViewSet)
router.register(r"about-us", DocumentViewSet)
router.register(r"about-us", OrganizationDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
