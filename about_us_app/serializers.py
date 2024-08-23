from rest_framework import serializers
from .models import TeamMember, Document, OrganizationDetail


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class OrganizationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDetail
        fields = '__all__'


class CombinedSerializer(serializers.Serializer):
    team = TeamMemberSerializer(many=True)
    doc = DocumentSerializer(many=True)
    org = OrganizationDetailSerializer(many=True)