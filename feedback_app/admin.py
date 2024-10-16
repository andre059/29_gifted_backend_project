from django.contrib import admin

from feedback_app.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("name", "lastname", "truncated_field", "link")
    search_fields = ("name", "lastname")

    def truncated_field(self, obj):
        return obj.content[:40] + ("..." if len(obj.content) > 40 else "")
