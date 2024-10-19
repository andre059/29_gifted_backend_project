from django.contrib import admin
from projects_app.models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name", "truncated_field",
    )
    search_fields = (
        "name",
        )
    inlines = [
        ProjectImageInline,
    ]

    def truncated_field(self, obj):
        return obj.content[:40] + ("..." if len(obj.content) > 40 else "")
