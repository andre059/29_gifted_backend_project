from rest_framework import viewsets
from .models import TeamMember
from .serializers import TeamMemberSerializer

class TeamMemberViewSet(viewsets.ModelViewSet):
    """ API view for team members """
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
