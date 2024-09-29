from django.contrib import admin
from .models import ContactPage

@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('header', 'address', 'email', 'phones', 'for_media', 'photo_thumbnail')
    search_fields = ('header', 'address', 'email', 'phones', 'for_media')
    list_filter = ('header', 'address', 'email')
    readonly_fields = ('photo_thumbnail',)
    
    fieldsets = (
        (None, {
            'fields': ('header', 'photo', 'photo_thumbnail')
        }),
        ('Контактная информация', {
            'fields': ('short_description', 'address', 'phones', 'email', 'for_media')
        }),
    )
    
    def photo_thumbnail(self, obj):
        if obj.photo:
            return f'<img src="{obj.photo.url}" width="100" height="100" />'
        return "Нет изображения"
    photo_thumbnail.allow_tags = True
    photo_thumbnail.short_description = 'фото'

