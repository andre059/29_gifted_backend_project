from rest_framework import serializers
from assistance_form_app.models import AssistanceForm
from config.services import fix_phone

class AssistanceFormSerializer(serializers.ModelSerializer):
    
    def validate_phone(self, value):
        return fix_phone(value)

    class Meta:
        model = AssistanceForm
        fields = "__all__"