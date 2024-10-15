from django.urls import path

from transfer_app.apps import PaymentAppConfig
from transfer_app.views import PaymentFormView, PaymentRedirectView, PaymentStatusView

app_name = PaymentAppConfig.name

urlpatterns = [
    path('payment-form/', PaymentFormView.as_view(), name='payment_form'),
    path('payment-redirect/', PaymentRedirectView.as_view(), name='payment_redirect'),
    path('payment-status/', PaymentStatusView.as_view(), name='payment_status'),

    # path('payment/create/', CreatePaymentView.as_view(), name='payment-create'),
    # path('payment/acceptance/', CreatePaymentAcceptanceView.as_view(), name='payment-acceptance'),
    # path('recurring_payment/', CreateRecurringPaymentView.as_view(), name='create_recurring_payment'),
    # path('recurring_payment/<int:payment_id>/', CancelRecurringPaymentView.as_view(), name='cancel_recurring_payment'),
]
