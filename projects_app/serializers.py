from rest_framework import serializers
from config.utils import replace_http_to_https_in_link
from projects_app.models import Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)
    
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
