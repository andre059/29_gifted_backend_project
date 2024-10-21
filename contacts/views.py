from rest_framework import viewsets
from .models import ContactPage
from .serializers import ContactPageSerializer


class ContactPageViewSet(viewsets.ModelViewSet):
    queryset = ContactPage.objects.all()
    serializer_class = ContactPageSerializer
    http_method_names = ["get"]
