from django.contrib import admin
from .models import ContactPage

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('address', 'email', 'phones',)
    search_fields = ('address', 'email', 'phones',)
    list_filter = ( 'address', 'email')
