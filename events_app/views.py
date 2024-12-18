from django.core.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response

from django.core.mail import send_mail
from rest_framework import viewsets, status
from .models import Event, Registration
from .serializers import EventsSerializer, RegistrationSerializer


class EventsAPIView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    http_method_names = ["get"]


class RegistrationsAPIView(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    http_method_names = ["get", "post"]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                event_id = request.data.get("event")
                event = Event.objects.get(pk=event_id)
                registration = serializer.save(event=event)
                self.send_registration_email(registration)
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED,
                    )
            except ValidationError as e:
                return Response(
                    { "error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                    )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=["post"])
    def register(self, request):
        return self.post(request)

    @classmethod
    def send_registration_email(cls, registration):

        subject = f"Регистрация на мероприятие: {registration.event.name_of_event}"
        message = f"Заявка на регистрацию от {registration.first_name} {registration.last_name}\n\n" \
                  f"Телефон: {registration.phone}\n" \
                  f"Email: {registration.email}\n" \
                  f"Комментарий: {registration.comment}\n"
        from_email = "noreply@yourdomain.com"  
        to_email = registration.email
        send_mail(subject, message, from_email, [to_email])
