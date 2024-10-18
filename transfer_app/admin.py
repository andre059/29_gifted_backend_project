from django.contrib import admin

from transfer_app.models import PaymentModel


@admin.register(PaymentModel)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'email', 'transfer_amount',
                    'comment', 'created_at', 'updated_at')
    list_filter = ('name', 'surname')
