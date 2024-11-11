from rest_framework import serializers
from .models import TeamMember, Document, OrganizationDetail, UserAgreement


class TeamMemberSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link and isinstance(representation.get('link'), str):
            representation['link'] = representation['link'].replace('http://', 'https://')
        return representation
    
    class Meta:
        model = TeamMember
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link:
            representation['link'] = self.replace_http_with_https(representation['link'])
        return representation
    
    class Meta:
        model = Document
        fields = "__all__"

class UserAgreementSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link:
            representation['link'] = self.replace_http_with_https(representation['link'])
        return representation
    
    class Meta:
        model = UserAgreement
        fields = "__all__"


class OrganizationDetailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.link:
            representation['link'] = self.replace_http_with_https(representation['link'])
        return representation
    
    class Meta:
        model = OrganizationDetail
        fields = "__all__"


class CombinedSerializer(serializers.Serializer):
    team = TeamMemberSerializer(many=True)
    doc = DocumentSerializer(many=True)
    org = OrganizationDetailSerializer(many=True)
