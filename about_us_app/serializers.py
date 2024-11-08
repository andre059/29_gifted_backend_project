from rest_framework import serializers
from .models import TeamMember, Document, OrganizationDetail
from config.utils import replace_http_to_https_in_link


class TeamMemberSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)
    
    class Meta:
        model = TeamMember
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)
    
    class Meta:
        model = Document
        fields = "__all__"


class OrganizationDetailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return replace_http_to_https_in_link(instance)
    
    class Meta:
        model = OrganizationDetail
        fields = "__all__"


class CombinedSerializer(serializers.Serializer):
    team = TeamMemberSerializer(many=True)
    doc = DocumentSerializer(many=True)
    org = OrganizationDetailSerializer(many=True)
