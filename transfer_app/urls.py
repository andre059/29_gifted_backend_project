from django.urls import path

from transfer_app.apps import PaymentAppConfig
from transfer_app.views import PaymentFormView, PaymentProcessingView, PaymentSuccessView

app_name = PaymentAppConfig.name

urlpatterns = [
    path('payment-form/', PaymentFormView.as_view(), name='payment_form'),
    path('payment-processing/', PaymentProcessingView.as_view(), name='payment_processing'),
    path('payment-status/', PaymentSuccessView.as_view(), name='payment_success'),
]
