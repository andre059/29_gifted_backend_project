from rest_framework import serializers
from assistance_form_app.models import AssistanceForm

class AssistanceFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssistanceForm
        fields = "__all__"