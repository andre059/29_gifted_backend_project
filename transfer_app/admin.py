from django.contrib import admin

from transfer_app.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'amount', 'currency', 'status')
    list_filter = ('status',)
