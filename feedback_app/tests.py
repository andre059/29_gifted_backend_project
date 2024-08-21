from rest_framework import status
from rest_framework.test import APITestCase
from feedback_app.models import Feedback
from django.urls import reverse


class FeedbackAPITestCase(APITestCase):

    def setUp(self):
        self.feedback = Feedback.objects.create(
            name='Тест',
            lastname='Тестов',
            surname='Тестович',
            content='Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        )

    def test_create_feedback(self):
        """Функция для тестирования создания отзыва"""
        data = {
            'name':'Тест',
            'lastname':'Тестов',
            'surname':'Тестович',
            'content':'Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        }
        response = self.client.post(
            reverse('feedback_app:feedback-list'),
            data=data,
        )
        #print(response.json())
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Feedback.objects.all().exists()
        )


    def test_list_events(self):
        """ Функция тестирования получения списка отзывов"""

        Feedback.objects.create(
            name='Тест1',
            lastname='Тестов',
            surname='Тестович',
            content='Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        )
        Feedback.objects.create(
            name='Тест2',
            lastname='Тестов',
            surname='Тестович',
            content='Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        )
        Feedback.objects.create(
            name='Тест3',
            lastname='Тестов',
            surname='Тестович',
            content='Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        )

        # Test pagination
        response = self.client.get(
            reverse('feedback_app:feedback-list'),
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


    def test_retrieve_events(self):
        """Функция тестирования получения одного отзыва"""

        response = self.client.get(
            reverse('feedback_app:feedback-detail', args=[self.feedback.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['name'], 'Тест'
        )


    def test_update_events(self):
        """Функция тестирования редактирования отзыва"""

        updated_data = {
            'name': 'Новый тест'
        }

        response = self.client.patch(
            reverse('feedback_app:feedback-detail', args=[self.feedback.id]),
            updated_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_destroy_events(self):
        """Функция тестирования удаления отзыва"""

        response = self.client.delete(
                reverse('feedback_app:feedback-detail', args=[self.feedback.id]),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Feedback.objects.filter(pk=self.feedback.id).exists()
        )
