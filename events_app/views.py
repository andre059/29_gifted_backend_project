from rest_framework import generics
from rest_framework.permissions import AllowAny

from events_app.models import Events
from events_app.paginators import EducationPaginator
from events_app.serliazers import EventsSerializer


class EventsCreateAPIView(generics.CreateAPIView):

    serializer_class = EventsSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_event = serializer.save()
        new_event.save()


class EventsListAPIView(generics.ListAPIView):

    serializer_class = EventsSerializer
    permission_classes = [AllowAny]
    queryset = Events.objects.all()
    pagination_class = EducationPaginator


class EventsRetriveAPIView(generics.RetrieveAPIView):

    serializer_class = EventsSerializer
    permission_classes = [AllowAny]
    queryset = Events.objects.all()


class EventsUpdateAPIView(generics.UpdateAPIView):

    serializer_class = EventsSerializer
    queryset = Events.objects.all()
    permission_classes = [AllowAny]


class EventsDestroyAPIView(generics.DestroyAPIView):

    serializer_class = EventsSerializer
    permission_classes = [AllowAny]
    queryset = Events.objects.all()
