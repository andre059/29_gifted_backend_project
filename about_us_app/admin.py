from django.contrib import admin

from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'role', 'photo')
    search_fields = ('name', 'last_name', 'role')
   