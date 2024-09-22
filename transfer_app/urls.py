from django.urls import path, include
from rest_framework.routers import DefaultRouter

from transfer_app.apps import PaymentAppConfig
from transfer_app.views import PaymentViewSet


app_name = PaymentAppConfig.name
router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
]
