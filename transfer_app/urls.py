from django.urls import path

from transfer_app.apps import PaymentAppConfig
from transfer_app.views import CreatePaymentView, CreatePaymentAcceptanceView

app_name = PaymentAppConfig.name

urlpatterns = [
    path('payment/', CreatePaymentView.as_view(), name='payment-create'),
    path('payment/acceptance/', CreatePaymentAcceptanceView.as_view(), name='payment-acceptance'),
]
