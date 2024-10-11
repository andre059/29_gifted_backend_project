from django.urls import path

from transfer_app.apps import PaymentAppConfig
from transfer_app.views import CreatePaymentView, CreatePaymentAcceptanceView, CreateRecurringPaymentView, \
    CancelRecurringPaymentView

app_name = PaymentAppConfig.name

urlpatterns = [
    path('payment/', CreatePaymentView.as_view(), name='payment-create'),
    path('payment/acceptance/', CreatePaymentAcceptanceView.as_view(), name='payment-acceptance'),
    path('recurring_payment/', CreateRecurringPaymentView.as_view(), name='create_recurring_payment'),
    path('recurring_payment/<int:payment_id>/', CancelRecurringPaymentView.as_view(), name='cancel_recurring_payment'),
]
