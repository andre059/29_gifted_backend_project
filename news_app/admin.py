from django import forms
from django.contrib import admin
from .models import News, NewsImage

class DeleteMixin:
    delete = forms.BooleanField(
        required=False, initial=False, label="Удалить",
        )


class NewsImageForm(forms.ModelForm, DeleteMixin):
    delete = forms.BooleanField(
        required=False, initial=False, label="Удалить",
        )

    class Meta:
        model = NewsImage
        fields = [
            "link",
            ]


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"

    def save_new_image(self, form, commit=True):
        if form.cleaned_data.get("delete"):
            form.instance.delete()
        else:
            return super().save_new_image(form, commit=commit)


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title", "short_description",
             "content", "video",
             ]

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ["custom_title"]
    inlines = [NewsImageInline]
    readonly_fields = ["created_at"]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        return [
            "created_at", "title", "content", 
            "video", "short_description",
            ]

    def get_queryset(self, request):
        return super().get_queryset(request)

    def custom_title(self, obj):
        return obj.title
    custom_title.short_description = "Новость"
