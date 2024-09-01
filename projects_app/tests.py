from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase
from projects_app.models import Project
from django.urls import reverse


class ProjectAPITestCase(APITestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name='Тест',
            content='Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        )

    def test_create_project(self):
        """Функция для тестирования создания проекта"""
        data = {
            'name':'Тест',
            'content':'Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        }
        response = self.client.post(
            reverse('projects_app:project-list'),
            data=data,
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Project.objects.all().exists()
        )


    def test_list_projects(self):
        """ Функция тестирования получения списка проектов"""

        Project.objects.create(
            name='Тест1',
            content='Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        )
        Project.objects.create(
            name='Тест2',
            content='Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        )
        Project.objects.create(
            name='Тест3',
            content='Тест тест тест тест тест тест тест тест тест тест тест тест тест',
        )

        response = self.client.get(
            reverse('projects_app:project-list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIsNone(
            response.json()['previous']
        )


    def test_retrieve_project(self):
        """Функция тестирования получения одного проекта"""

        response = self.client.get(
            reverse('projects_app:project-detail', args=[self.project.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['name'], 'Тест'
        )


    def test_update_project(self):
        """Функция тестирования редактирования проекта"""

        updated_data = {
            'name': 'Новыйтест'
        }

        response = self.client.patch(
            reverse('projects_app:project-detail', args=[self.project.id]),
            updated_data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_project(self):
        """Функция тестирования удаления проекта"""

        response = self.client.delete(
                reverse('projects_app:project-detail', args=[self.project.id]),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Project.objects.filter(pk=self.project.id).exists()
        )
