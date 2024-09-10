from django.contrib import messages
from rest_framework.response import Response

from django.core.mail import send_mail
from rest_framework import viewsets, status
from .models import Event, Registration
from .serializers import EventsSerializer, RegistrationSerializer


class EventsAPIView(viewsets.ModelViewSet):
    """ API view for events """
    queryset = Event.objects.all()
    serializer_class = EventsSerializer


class RegistrationsAPIView(viewsets.ModelViewSet):
    """ API for registration """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, args, kwargs):
        """ Redefining the create method for registration processing """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        event_id = request.data.get('event')
        event = Event.objects.get(pk=event_id)  # Получаем  событие
        registration = serializer.save(event=event)  # Сохраняем  регистрацию

        # Отправка письма
        self.send_registration_email(registration)

        # Успешная  регистрация
        messages.success(request, "Вы успешно зарегистрировались на мероприятие!")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def send_registration_email(self, registration):
        subject = f"Регистрация на мероприятие: {registration.event.name_of_event}"
        message = f"Заявка на регистрацию от {registration.first_name} {registration.last_name}\n\n" \
                  f"Телефон: {registration.phone}\n" \
                  f"Email: {registration.email}\n" \
                  f"Комментарий: {registration.comment}\n"
        from_email = "noreply@yourdomain.com"  # Замените на адрес отправителя письма
        to_email = registration.email  # Адрес получателя письма
        send_mail(subject, message, from_email, [to_email])
