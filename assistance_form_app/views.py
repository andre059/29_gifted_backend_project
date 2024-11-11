from assistance_form_app.models import AssistanceForm
from assistance_form_app.serializers import AssistanceFormSerializer
from rest_framework import viewsets


class AssistanceFormAPIView(viewsets.ModelViewSet):
    queryset = AssistanceForm.objects.all()
    serializer_class = AssistanceFormSerializer
    http_method_names = [
        "get", "post"
        ]