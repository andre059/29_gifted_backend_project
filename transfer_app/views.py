import uuid

from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView
from yookassa import Payment

from config import settings
from transfer_app.models import PaymentModel
from transfer_app.serializers import PaymentFormSerializer, PaymentSerializer
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
                name=data['name'],
                surname=data['surname'],
                telephone=data['telephone'],
                email=data['email'],
                transfer_amount=data['transfer_amount'],
                payment_frequency=data['payment_frequency'],
                type_transfer=data['type_transfer'],
                comment=data['comment']
            )

            return Response({"payment_id": payment_id, "type_transfer": data['type_transfer']}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentRedirectView(APIView):
    """Redirecting the user to the Yukassa payment system page"""

    serializer_class = PaymentSerializer

    def post(self, request):
        try:
            payment_id = request.data.get('payment_id')
            if not payment_id:
                raise ValidationError("Требуется идентификатор платежа")

            payment = PaymentModel.objects.get(payment_id=payment_id)
            if payment.status != 'pending':
                raise ValidationError("Платеж еще не произведен")

            config = setup_yandex_config(settings.YANDEX_ACCOUNT_ID, settings.YANDEX_SECRET_KEY)

            transfer_amount = float(payment.transfer_amount)
            if transfer_amount > 1000000:  # Предположим, это максимально допустимая сумма
                raise ValidationError("Превышено максимально допустимое количество")

            Payment.create({
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
            raise APIException("Платеж не найден", code="payment_not_found")
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymentStatusView(APIView):
    """Checking the payment status and updating it in the database"""

    serializer_class = PaymentSerializer

    def get(self, request):
        request_status = request.query_params.get('status')
        payment_id = request.query_params.get('id')

        if request_status == 'success':
            try:
                # Ищем платеж по ID
                payment = PaymentModel.objects.get(payment_id=payment_id)
                # Обновляем статус платежа
                payment.status = 'successful'
                payment.save()

                # Возвращаем данные об обновленном платеже
                return Response(PaymentSerializer(payment).data, status=status.HTTP_200_OK)
            except PaymentModel.DoesNotExist:
                # Если платеж не найден, возвращаем ошибку
                return Response({"error": "Платеж не найден"}, status=status.HTTP_404_NOT_FOUND)

        # Если статус не равен 'success', возвращаем ошибку
        return Response({"error": "Платеж не состоялся"}, status=status.HTTP_400_BAD_REQUEST)
