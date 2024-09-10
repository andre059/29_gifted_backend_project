from django.contrib import admin

from transfer_app.models import Transfer


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'amount', 'currency', 'status')
    list_filter = ('status',)
