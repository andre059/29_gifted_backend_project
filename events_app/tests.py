from datetime import datetime, timezone, timedelta

from rest_framework import status
from rest_framework.test import APITestCase

from events_app.models import Events


class EventsAPITestCase(APITestCase):

    def setUp(self):
        self.events = Events.objects.create(
            name_of_event='Тестовое мероприятие 1',
            description_of_event='Тестовое описание 1',
            address_of_event='Санкт-Петербург, ул. Ленина, д.1',
            date_time_of_event=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(hours=3))),
        )

    def test_create_event(self):
        """ Testing creating an event """
        data = {
            'name_of_event': 'Тестовое мероприятие',
            'description_of_event': 'Тестовое описание',
            'address_of_event': 'Санкт-Петербург, ул. Ленина, д.1',
            'date_time_of_event': '2020-01-01T00:00:00',
        }
        response = self.client.post(
            '/events/create/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        expected_datetime = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(hours=3)))
        self.assertEqual(
            response.json(),
            {
                'id': 2,
                'name_of_event': 'Тестовое мероприятие',
                'description_of_event': 'Тестовое описание',
                'address_of_event': 'Санкт-Петербург, ул. Ленина, д.1',
                'date_time_of_event': expected_datetime.isoformat(),
            }
        )

        self.assertTrue(
            Events.objects.all().exists()
        )

    def test_list_events(self):
        """ Testing getting list of events """

        Events.objects.create(
            name_of_event='Тестовое мероприятие 1',
            description_of_event='Тестовое описание 1',
            address_of_event='Санкт-Петербург, ул. Ленина, д.1',
            date_time_of_event=datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone(timedelta(hours=3))),
        )
        Events.objects.create(
            name_of_event='Тестовое мероприятие 2',
            description_of_event='Тестовое описание 2',
            address_of_event='Санкт-Петербург, ул. Ленина, д.2',
            date_time_of_event=datetime(2021, 2, 2, 1, 1, 1, tzinfo=timezone(timedelta(hours=3))),
        )
        Events.objects.create(
            name_of_event='Тестовое мероприятие 3',
            description_of_event='Тестовое описание 3',
            address_of_event='Санкт-Петербург, ул. Ленина, д.3',
            date_time_of_event=datetime(2022, 3, 3, 2, 2, 2, tzinfo=timezone(timedelta(hours=3))),
        )

        # Test pagination
        response = self.client.get(
            '/events/list/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            len(response.json()['results']),
            3
        )

        self.assertIsNone(
            response.json()['previous']
        )

        response = self.client.get(
            '/events/list/100/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_retrieve_events(self):
        """ Testing getting one event """

        response = self.client.get(
            f'/events/{self.events.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['name_of_event'], 'Тестовое мероприятие 1'
        )
        self.assertEqual(
            response.data['description_of_event'], 'Тестовое описание 1'
        )
        self.assertEqual(
            response.data['address_of_event'], 'Санкт-Петербург, ул. Ленина, д.1'
        )
        self.assertEqual(
            response.data['date_time_of_event'], '2020-01-01T00:00:00+03:00'
        )

    def test_update_events(self):
        """ Testing updating an event """

        data = {
            'name_of_event': 'Тестовое мероприятие 4'
        }

        response = self.client.patch(
            f'/events/update/{self.events.id}/',
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['name_of_event'], 'Тестовое мероприятие 4'
        )

    def test_destroy_events(self):
        """ Testing deleting an event """

        response = self.client.delete(
                f'/events/delete/{self.events.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Events.objects.filter(pk=self.events.id).exists()
        )
