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








# class EventsAPITestCase(APITestCase):
#
#     def setUp(self):
#         self.events = Events.objects.create(
#             name_of_event='Тестовое мероприятие 1',
#             description_of_event='Тестовое описание 1',
#             address_of_event='Санкт-Петербург, ул. Ленина, д.1',
#             date_time_of_event=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(hours=3))),
#         )
#
#     def test_create_event(self):
#         """ Testing creating an event """
#         data = {
#             'name_of_event': 'Тестовое мероприятие',
#             'description_of_event': 'Тестовое описание',
#             'address_of_event': 'Санкт-Петербург, ул. Ленина, д.1',
#             'date_time_of_event': '2020-01-01T00:00:00',
#         }
#         response = self.client.post(
#             '/events/create/',
#             data=data,
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_201_CREATED
#         )
#
#         expected_datetime = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(hours=3)))
#         self.assertEqual(
#             response.json(),
#             {
#                 'id': 2,
#                 'name_of_event': 'Тестовое мероприятие',
#                 'description_of_event': 'Тестовое описание',
#                 'address_of_event': 'Санкт-Петербург, ул. Ленина, д.1',
#                 'date_time_of_event': expected_datetime.isoformat(),
#             }
#         )
#
#         self.assertTrue(
#             Events.objects.all().exists()
#         )
#
#     def test_list_events(self):
#         """ Testing getting list of events """
#
#         Events.objects.create(
#             name_of_event='Тестовое мероприятие 1',
#             description_of_event='Тестовое описание 1',
#             address_of_event='Санкт-Петербург, ул. Ленина, д.1',
#             date_time_of_event=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(hours=3))),
#         )
#         Events.objects.create(
#             name_of_event='Тестовое мероприятие 2',
#             description_of_event='Тестовое описание 2',
#             address_of_event='Санкт-Петербург, ул. Ленина, д.2',
#             date_time_of_event=datetime(2021, 2, 2, 1, 1, 1, tzinfo=timezone(timedelta(hours=3))),
#         )
#         Events.objects.create(
#             name_of_event='Тестовое мероприятие 3',
#             description_of_event='Тестовое описание 3',
#             address_of_event='Санкт-Петербург, ул. Ленина, д.3',
#             date_time_of_event=datetime(2022, 3, 3, 2, 2, 2, tzinfo=timezone(timedelta(hours=3))),
#         )
#
#         # Test pagination
#         response = self.client.get(
#             '/events/list/'
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#
#         self.assertEqual(
#             len(response.json()['results']),
#             3
#         )
#
#         self.assertIsNone(
#             response.json()['previous']
#         )
#
#         response = self.client.get(
#             '/events/list/100/'
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_404_NOT_FOUND
#         )
#
#     def test_retrieve_events(self):
#         """ Testing getting one event """
#
#         response = self.client.get(
#             f'/events/{self.events.id}/'
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#
#         self.assertEqual(
#             response.data['name_of_event'], 'Тестовое мероприятие 1'
#         )
#         self.assertEqual(
#             response.data['description_of_event'], 'Тестовое описание 1'
#         )
#         self.assertEqual(
#             response.data['address_of_event'], 'Санкт-Петербург, ул. Ленина, д.1'
#         )
#         self.assertEqual(
#             response.data['date_time_of_event'], '2020-01-01T00:00:00+03:00'
#         )
#
#     def test_update_events(self):
#         """ Testing updating an event """
#
#         data = {
#             'name_of_event': 'Тестовое мероприятие 4'
#         }
#
#         response = self.client.patch(
#             f'/events/update/{self.events.id}/',
#             data=data,
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#
#         self.assertEqual(
#             response.data['name_of_event'], 'Тестовое мероприятие 4'
#         )
#
#     def test_destroy_events(self):
#         """ Testing deleting an event """
#
#         response = self.client.delete(
#                 f'/events/delete/{self.events.id}/',
#         )
#
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_204_NO_CONTENT
#         )
#
#         self.assertFalse(
#             Events.objects.filter(pk=self.events.id).exists()
#         )
