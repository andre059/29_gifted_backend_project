from rest_framework import viewsets
from .models import Developer
from .serializers import DeveloperSerializer

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    http_method_names = ["get"]

