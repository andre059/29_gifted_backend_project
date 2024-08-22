from rest_framework import viewsets
from .models import TeamMember, Document, OrganizationDetail
from .serializers import (
    TeamMemberSerializer,
    DocumentSerializer,
    OrganizationDetailSerializer,
)


class TeamMemberViewSet(viewsets.ModelViewSet):
    """ API view for team members """
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class OrganizationDetailViewSet(viewsets.ModelViewSet):
    queryset = OrganizationDetail.objects.all()
    serializer_class = OrganizationDetailSerializer
