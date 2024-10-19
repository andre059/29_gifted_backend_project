from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from transfer_app.models import PaymentModel
from transfer_app.serializers import PaymentFormSerializer
from transfer_app.utils import create_payment, set_payment_status
from rest_framework.request import Request


class PaymentFormView(APIView):

    serializer_class = PaymentFormSerializer

    def post(self, request: Request):
        serializer = PaymentFormSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            payment = create_payment(data['transfer_amount'], data['comment'])
            
            PaymentModel.objects.create(
                payment_id=payment.id,
                name=data['name'],
                last_name=data['last_name'],
                phone=data['phone'],
                email=data['email'],
                transfer_amount=data['transfer_amount'],
                comment=data['comment']
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

    def post(self, request: Request):
        try:
            payment = set_payment_status(request)
            return Response(
                {"payment_id": payment.payment_id, 
                 "payment_status": payment.status}, 
                 status=status.HTTP_200_OK,
                 )
        except ValidationError as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST,
                )


# class PaymentSuccessView(APIView):

#     def post(self, request: Request):
#         try:
#             payment = set_payment_status(request)
#             if payment.status == 'succeeded':
#                 return Response({"payment_id": payment.payment_id, "payment_status": payment.status}, status=status.HTTP_200_OK)
#             else:
#                 return Response({"payment_id": payment.payment_id, "payment_status": payment.status}, status=status.HTTP_400_BAD_REQUEST)
#         except ValidationError as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
