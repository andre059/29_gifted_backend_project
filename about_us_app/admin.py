from django.contrib import admin
from .models import TeamMember, CategoryDocument, Document, OrganizationDetail


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "role", "photo")
    search_fields = ("name", "last_name", "role")


@admin.register(CategoryDocument)
class CategoryDocumentAdmin(admin.ModelAdmin):
    list_display = ("name",)


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
        "director",
        "link",
    )
