from rest_framework import serializers
from projects_app.models import Project, ProjectImage

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image']


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    """Сериализатор для проектов"""
    class Meta:
        model = Project
        fields = '__all__'
