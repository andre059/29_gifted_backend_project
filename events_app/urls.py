from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events_app.apps import EventsAppConfig
from events_app.views import EventsAPIView, RegistrationsAPIView

app_name = EventsAppConfig.name

router = DefaultRouter()
router.register(r'events', EventsAPIView, basename='event')
router.register(r'registrations', RegistrationsAPIView, basename='registration')

urlpatterns = [
    path('', include(router.urls)),
    ]
