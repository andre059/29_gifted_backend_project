from rest_framework import viewsets
from .models import Event
from .serializers import EventsSerializer


class EventsAPIView(viewsets.ModelViewSet):
    """ API view for events """
    queryset = Event.objects.all()
    serializer_class = EventsSerializer

