from django.contrib import admin

from assistance_form_app.models import AssistanceForm


@admin.register(AssistanceForm)
class AssistanceFormAdmin(admin.ModelAdmin):
    list_display = (
        "name", "lastname",
         "phone", "email",
         )
    search_fields = (
        "name", "lastname",
        )