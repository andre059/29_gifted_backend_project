from django.contrib import admin

from transfer_app.models import PaymentModel


@admin.register(PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'telephone', 'email', 'transfer_amount', 'transfer_type', 'comment',
                    'created_at', 'updated_at')
    list_filter = ('name', 'surname')
