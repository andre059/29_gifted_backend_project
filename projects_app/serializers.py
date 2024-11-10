from rest_framework import serializers
from projects_app.models import Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link and isinstance(representation.get('link'), str):
            representation['link'] = representation['link'].replace('http://', 'https://')
        return representation
    
    class Meta:
        model = ProjectImage
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(
        many=True, read_only=True,
        )

    class Meta:
        model = Project
        fields = "__all__"
