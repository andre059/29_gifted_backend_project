import json
import uuid

from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from yookassa import Payment

from config import settings
from transfer_app.models import PaymentModel
from transfer_app.serializers import PaymentFormSerializer, PaymentSerializer
# from transfer_app.services.create_payment import create_payment
# from transfer_app.services.payment_acceptance import payment_acceptance
from transfer_app.utils import generate_payment_id, setup_yandex_config


class PaymentFormView(APIView):
    """Sending the payment form"""

    serializer_class = PaymentFormSerializer

    def post(self, request):
        serializer = PaymentFormSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            payment_id = generate_payment_id(float(data['transfer_amount']))

            PaymentModel.objects.create(
                payment_id=payment_id,
                amount=data['transfer_amount'],
                transfer_type=data['transfer_type'],
                comment=data['comment']
            )

            return Response({"message": "Payment form submitted successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentRedirectView(APIView):
    """Redirecting the user to the Yukassa payment system page"""

    serializer_class = PaymentSerializer

    def post(self, request):
        try:
            payment_id = request.data.get('payment_id')
            if not payment_id:
                raise ValidationError("Payment ID is required")

            payment = PaymentModel.objects.get(payment_id=payment_id)
            if payment.status != 'pending':
                raise ValidationError("Payment is not pending")

            config = setup_yandex_config(settings.YANDEX_ACCOUNT_ID, settings.YANDEX_SECRET_KEY)

            transfer_amount = float(payment.transfer_amount)
            if transfer_amount > 1000000:  # Предположим, это максимально допустимая сумма
                raise ValidationError("Maximum allowed amount exceeded")

            payment = config.Payment.create({
                "amount": {
                    "value": str(transfer_amount),
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": f"{settings.SITE_URL}/payment-status/{payment_id}"
                },
                "capture": True,
                "description": f"Платеж на сумму {transfer_amount} руб."
            }, uuid.uuid4())

            payment.status = 'processing'
            payment.save()

            return Response({"payment_id": payment.payment_id}, status=status.HTTP_200_OK)

        except PaymentModel.DoesNotExist:
            raise APIException("Payment not found", code="payment_not_found")
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymentStatusView(APIView):
    """Checking the payment status and updating it in the database"""

    serializer_class = PaymentSerializer

    def get(self, request):
        status = request.query_params.get('status')
        payment_id = request.query_params.get('id')

        if status == 'success':
            try:
                payment = PaymentModel.objects.get(payment_id=payment_id)
                payment.status = 'successful'
                payment.save()
                return Response(PaymentSerializer(payment).data, status=status.HTTP_200_OK)
            except PaymentModel.DoesNotExist:
                return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": "Payment failed"}, status=status.HTTP_400_BAD_REQUEST)


# class CreatePaymentView(CreateAPIView):
#     serializer_class = CreatePaymentSerializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#
#         with transaction.atomic():
#             if serializer.is_valid(raise_exception=True):
#                 validated_data = serializer.validated_data
#                 confirmation_url = create_payment(validated_data)
#
#                 return Response({'confirmation_url': confirmation_url}, status=status.HTTP_201_CREATED)
#
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # def post(self, request, *args, **kwargs):
#     #     serializer = CreatePaymentSerializer(data=request.data)
#     #
#     #     if serializer.is_valid():
#     #         serialized_data = serializer.validated_data
#     #     else:
#     #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #
#     #     confirmation_url = create_payment(serialized_data)
#     #
#     #     return Response({'confirmation_url': confirmation_url}, 200)
#
#
# class CreatePaymentAcceptanceView(CreateAPIView):
#
#     def post(self, request, *args, **kwargs):
#         response = json.loads(request.body)
#
#         if payment_acceptance(response):
#             return Response(200)
#         return Response(404)
#
#
# class CreateRecurringPaymentView(CreateAPIView):
#     def post(self, request):
#         # Получите данные о платеже
#         serializer = CreateRecurringPaymentSerializer(data=request.data)
#         if serializer.is_valid():
#             serialized_data = serializer.validated_data
#             payment = Payment.objects.create(
#                 transfer_amount=serialized_data['amount'],
#                 name="Имя",
#                 surname="Фамилия",
#                 telephone="+71234567890",
#                 email="test@example.com",
#                 type_transfer='using your phone',
#                 comment="Комментарий",
#             )
#             recurring_payment = RecurringPayment.objects.create(
#                 payment=payment,
#                 amount=serialized_data['amount'],
#                 frequency=serialized_data['frequency'],
#                 next_payment_date=serialized_data['next_payment_date'],
#             )
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CancelRecurringPaymentView(CreateAPIView):
#     """Отменить платеж"""
#
#     def post(self, request, payment_id):
#         try:
#             recurring_payment = RecurringPayment.objects.get(payment__payment_id=payment_id)
#         except RecurringPayment.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         recurring_payment.is_active = False
#         recurring_payment.save()
#
#         return Response(status=status.HTTP_200_OK)
