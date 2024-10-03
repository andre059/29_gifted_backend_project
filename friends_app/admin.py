from django.contrib import admin
from .models import Friend, Company, Volunteer


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "link", "description", "is_published")
    search_fields = ("name", "last_name", "is_published")
    fields = ("name", "last_name", "link", "description", "is_published", "gender")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "description", "is_published")
    search_fields = ("name",)
    fields = ("name", "link", "description", "is_published")


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "email", "is_accept")
    search_fields = ("name",)
