import os
import pytest

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from events_app.models import Event

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


class TestEventsAPI:
    client = APIClient()

    @staticmethod
    def create_test_event():
        # Создание тестового события для использования в тестах
        event = Event.objects.create(
            name_of_event='Тестовое мероприятие',
            description_of_event='Тестовое описание',
            address_of_event='Санкт-Петербург',
            date_time_of_event='2023-12-31T12:00:00',  # Формат ISO 8601
        )
        return event

    def test_list_events(self):
        self.create_test_event()
        response = self.client.get(reverse('events-app:events-list'))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['results'][0]['name_of_event'] == 'Тестовое мероприятие'

    def test_create_event(self):
        data = {
            'name_of_event': 'Новое мероприятие',
            'description_of_event': 'Описание нового мероприятия',
            'address_of_event': 'Москва',
            'date_time_of_event': '2024-01-01T12:00:00',
        }
        response = self.client.post(reverse('events-app:events-list'), data=data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name_of_event'] == 'Новое мероприятие'

    def test_retrieve_event(self):
        event = self.create_test_event()
        response = self.client.get(reverse('events-app:events-detail', args=[event.pk]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name_of_event'] == 'Тестовое мероприятие'

    def test_update_event(self):
        event = self.create_test_event()
        data = {
            'name_of_event': 'Обновленное мероприятие',
        }
        response = self.client.patch(reverse('events-app:events-detail', args=[event.pk]), data=data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name_of_event'] == 'Обновленное мероприятие'

    def test_delete_event(self):
        event = self.create_test_event()
        response = self.client.delete(reverse('events-app:events-detail', args=[event.pk]))
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Event.objects.filter(pk=event.pk).exists()
