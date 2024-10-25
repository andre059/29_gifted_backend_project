from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from transfer_app.models import PaymentModel
from transfer_app.serializers import PaymentSerializer
from transfer_app.utils import create_payment, set_payment_status
from rest_framework.request import Request


class PaymentFormView(APIView):
    serializer_class = PaymentSerializer
    http_method_names = ["post"]

    def post(self, request: Request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            payment = create_payment(
                data["transfer_amount"],
                data["comment"],
            )

            PaymentModel.objects.create(
                payment_id=payment.id,
                name=data["name"],
                last_name=data["last_name"],
                phone=data["phone"],
                email=data["email"],
                transfer_amount=data["transfer_amount"],
                comment=data["comment"]
            )

            return Response(
                {"payment_url": payment.confirmation.confirmation_url,
                 "payment_id": payment.id},
                status=status.HTTP_200_OK,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class PaymentProcessingView(APIView):
    http_method_names = ["post"]

    def post(self, request: Request):
        try:
            create_task = set_payment_status(request)
            return Response(
                create_task,
                status=status.HTTP_200_OK,
            )
        except ValidationError as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
