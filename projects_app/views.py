from projects_app.models import Project
from projects_app.serializers import ProjectSerializer
from rest_framework import viewsets


class ProjectAPIView(viewsets.ModelViewSet):
    """Функция для создания, редактирования и удаления проектов, а также
        просмотра всего списка проектов и просмотра отдельного проекта"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
