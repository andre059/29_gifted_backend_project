import json

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from yookassa import Payment

from transfer_app.models import RecurringPayment
from transfer_app.serializers import CreatePaymentSerializer, CreateRecurringPaymentSerializer
from transfer_app.services.create_payment import create_payment
from transfer_app.services.payment_acceptance import payment_acceptance


class CreatePaymentView(CreateAPIView):
    serializer_class = CreatePaymentSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreatePaymentSerializer(data=request.data)

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


class CreateRecurringPaymentView(CreateAPIView):
    def post(self, request):
        # Получите данные о платеже
        serializer = CreateRecurringPaymentSerializer(data=request.data)
        if serializer.is_valid():
            serialized_data = serializer.validated_data
            payment = Payment.objects.create(
                transfer_amount=serialized_data['amount'],
                name="Имя",
                surname="Фамилия",
                telephone="+71234567890",
                email="test@example.com",
                type_transfer='using your phone',
                comment="Комментарий",
            )
            recurring_payment = RecurringPayment.objects.create(
                payment=payment,
                amount=serialized_data['amount'],
                frequency=serialized_data['frequency'],
                next_payment_date=serialized_data['next_payment_date'],
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CancelRecurringPaymentView(CreateAPIView):
    """Отменить платеж"""

    def post(self, request, payment_id):
        try:
            recurring_payment = RecurringPayment.objects.get(payment__payment_id=payment_id)
        except RecurringPayment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        recurring_payment.is_active = False
        recurring_payment.save()

        return Response(status=status.HTTP_200_OK)
