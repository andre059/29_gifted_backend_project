from django.urls import path, include
from rest_framework.routers import DefaultRouter

from transfer_app.apps import TransferAppConfig
from transfer_app.views import TransferViewSet


app_name = TransferAppConfig.name
router = DefaultRouter()
router.register(r'transfers', TransferViewSet, basename='transfer')

urlpatterns = [
    path('', include(router.urls)),
]
