from django.urls import path

from events_app.apps import EventsAppConfig
from events_app.views import EventsCreateAPIView, EventsListAPIView, EventsRetriveAPIView, EventsUpdateAPIView, \
    EventsDestroyAPIView

app_name = EventsAppConfig.name

urlpatterns = [
    path('events/create/', EventsCreateAPIView.as_view(), name='events_create'),
    path('events/list/', EventsListAPIView.as_view(), name='events_list'),
    path('events/<int:pk>/', EventsRetriveAPIView.as_view(), name='events_detail'),
    path('events/update/<int:pk>/', EventsUpdateAPIView.as_view(), name='update'),
    path('events/delete/<int:pk>/', EventsDestroyAPIView.as_view(), name='delete'),
]
