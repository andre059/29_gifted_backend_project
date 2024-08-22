from django.contrib import admin

from events_app.models import Event, EventPhoto, EventVideo, EventLinkVideo


class EventPhotoInline(admin.TabularInline):
    model = EventPhoto
    extra = 1


class EventVideoInline(admin.TabularInline):
    model = EventVideo
    extra = 1


class EventLinkVideoInline(admin.TabularInline):
    model = EventLinkVideo
    extra = 1


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name_of_event', 'description_of_event', 'address_of_event', 'date_time_of_event')
    list_filter = ('name_of_event', 'description_of_event', 'address_of_event', 'date_time_of_event')
    inlines = [EventPhotoInline, EventVideoInline, EventLinkVideoInline]
