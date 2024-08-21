from rest_framework import viewsets
from .models import Events
from .serializers import EventsSerializer
from events_app.paginators import EventsPaginator

class EventsAPIView(viewsets.ModelViewSet):
    """ API view for events """
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    pagination_class = EventsPaginator