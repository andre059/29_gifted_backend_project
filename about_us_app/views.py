from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TeamMember, Document, OrganizationDetail
from .serializers import (
    TeamMemberSerializer,
    DocumentSerializer,
    OrganizationDetailSerializer,
    CombinedSerializer,
)


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.filter(is_published=True)
    serializer_class = TeamMemberSerializer
    http_method_names = ["get"]


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.filter(is_published=True)
    serializer_class = DocumentSerializer
    http_method_names = ["get"]


class OrganizationDetailViewSet(viewsets.ModelViewSet):
    queryset = OrganizationDetail.objects.filter(is_published=True)
    serializer_class = OrganizationDetailSerializer
    http_method_names = ["get"]


class CombinedDataView(APIView):
    http_method_names = ["get"]
    def get(self, request, *args, **kwargs):
        teams = TeamMember.objects.filter(is_published=True)
        docs = Document.objects.filter(is_published=True)
        orgs = OrganizationDetail.objects.filter(is_published=True)

        data = {
            "team": TeamMemberSerializer(teams, many=True).data,
            "doc": DocumentSerializer(docs, many=True).data,
            "org": OrganizationDetailSerializer(orgs, many=True).data,
        }

        serializer = CombinedSerializer(data=data)
        serializer.is_valid()
        return Response(serializer.data)
