from rest_framework import serializers
from projects_app.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Сериализатор для проектов"""
    class Meta:
        model = Project
        fields = '__all__'
