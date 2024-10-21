from rest_framework import viewsets
from .models import Friend, Company, Volunteer
from .serializers import (
    FriendSerializer,
    CompanySerializer,
    VolunteerSerializer,
)


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    http_method_names = ['get']


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['get']


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    http_method_names = [
        'get', 'post'
        ]
