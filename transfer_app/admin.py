from django.contrib import admin

from transfer_app.models import PaymentModel, RecurringPayment


@admin.register(PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'telephone', 'email', 'transfer_amount', 'type_transfer', 'comment',
                    'created_at', 'updated_at')
    list_filter = ('name', 'surname')


@admin.register(RecurringPayment)
class RecurringPaymentAdmin(admin.ModelAdmin):
    list_display = ('payment', 'amount', 'frequency', 'next_payment_date', 'is_active')
    list_filter = ('frequency', 'is_active')

