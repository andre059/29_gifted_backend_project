from rest_framework import serializers
from .models import TeamMember, Document, OrganizationDetail


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ["id", "name", "last_name", "role", "link"]


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ("id", "name", "category", "link", "description")


class OrganizationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDetail
        fields = (
            "id",
            "name",
            "legal_address",
            "ogrn_number",
            "inn_number",
            "kpp_number",
            "current_account",
            "address",
            "bik",
            "correspondent_account",
            "director",
            "link",
        )
