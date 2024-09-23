from rest_framework import viewsets
from transfer_app.models import Payment
from transfer_app.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """ API view for transfer """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
