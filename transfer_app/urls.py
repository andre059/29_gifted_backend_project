from django.urls import path

from transfer_app.apps import PaymentAppConfig
from transfer_app.views import PaymentFormView, PaymentRedirectView, PaymentStatusView

app_name = PaymentAppConfig.name

urlpatterns = [
    path('payment-form/', PaymentFormView.as_view(), name='payment_form'),
    path('payment-redirect/', PaymentRedirectView.as_view(), name='payment_redirect'),
    path('payment-status/', PaymentStatusView.as_view(), name='payment_status'),
]
