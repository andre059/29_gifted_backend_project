from django.contrib import admin
from .models import TeamMember, Document, OrganizationDetail


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "role", "link")
    search_fields = ("name", "last_name", "role", "is_published")


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "link", "description", "is_published")
    search_fields = ("name",)


@admin.register(OrganizationDetail)
class OrganizationDetailAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "legal_address",
        "address",
        "ogrn_number",
        "inn_number",
        "kpp_number",
        "current_account",
        "bik",
        "correspondent_account",
        "link",
        "is_published",
    )
