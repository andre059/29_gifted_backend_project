from projects_app.models import Project
from projects_app.serializers import ProjectSerializer
from rest_framework import viewsets


class ProjectAPIView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get']

