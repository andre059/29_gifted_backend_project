from django.contrib import admin
from projects_app.models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'truncated_field', 'preview')
    search_fields = ('name',)

    def truncated_field(self, obj):
        return obj.content[:40] + ('...' if len(obj.content) > 40 else '')
