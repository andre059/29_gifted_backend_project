from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events_app.apps import EventsAppConfig
from events_app.views import EventsAPIView


app_name = EventsAppConfig.name
router = DefaultRouter()
router.register(r'', EventsAPIView)

urlpatterns = [
    path('', include(router.urls)),
    ]
