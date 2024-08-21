from django.urls import path, include
from rest_framework.routers import DefaultRouter

from about_us_app.apps import AboutUsAppConfig
from .views import TeamMemberViewSet

app_name = AboutUsAppConfig.name
router = DefaultRouter()
router.register(r'', TeamMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
