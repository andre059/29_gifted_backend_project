# team/admin.py
from django.contrib import admin
from .models import Developer, DeveloperImage



class DeveloperImageInline(admin.TabularInline):
    model = DeveloperImage
    extra = 1


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "surname",
        "role",
    )
    search_fields = ("role",)
    inlines = [
        DeveloperImageInline,
    ]
