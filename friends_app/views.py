from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Friend, Company, Volunteer
from .forms import VolunteerForm
from .serializers import (
    FriendSerializer,
    CompanySerializer,
    VolunteerSerializer,
)


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
