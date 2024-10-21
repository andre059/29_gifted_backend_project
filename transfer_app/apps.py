from django.apps import AppConfig


class PaymentAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "transfer_app"
    verbose_name = "Платежи"
