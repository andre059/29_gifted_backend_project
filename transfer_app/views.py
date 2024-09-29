import json

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from transfer_app.serializers import CreatePaymentSerializer, CreateYooKassaPaymentSerializer
from transfer_app.services.create_payment import create_payment
from transfer_app.services.payment_acceptance import payment_acceptance


class CreatePaymentView(CreateAPIView):
    serializer_class = CreatePaymentSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateYooKassaPaymentSerializer(data=request.data)

        if serializer.is_valid():
            serialized_data = serializer.validated_data
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        confirmation_url = create_payment(serialized_data)

        return Response({'confirmation_url': confirmation_url}, 200)


class CreatePaymentAcceptanceView(CreateAPIView):

    def post(self, request, *args, **kwargs):
        response = json.loads(request.body)

        if payment_acceptance(response):
            return Response(200)
        return Response(404)
