from rest_framework import viewsets
from transfer_app.models import Transfer
from transfer_app.serializers import TransferSerializer


class TransferViewSet(viewsets.ModelViewSet):
    """ API view for transfer """

    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
