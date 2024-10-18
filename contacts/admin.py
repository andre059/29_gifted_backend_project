from django.contrib import admin
from .models import ContactPage


@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = (
        "address",
        "email",
        "phone_1",
        "phone_2",
        "phone_for_media",
        "email_for_media",
    )
    search_fields = (
        "address",
        "email",
        "phone_1",
        "phone_2",
        "phone_for_media",
        "email_for_media",
    )
    list_filter = (
        "address",
        "email",
        "phone_1",
        "phone_2",
        "phone_for_media",
        "email_for_media",
    )

    def has_add_permission(self, request):
        # Запрещаем добавление, если уже существует запись
        if ContactPage.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Запрещаем удаление, если запись существует
        if ContactPage.objects.exists():
            return False
        return super().has_delete_permission(request, obj)
