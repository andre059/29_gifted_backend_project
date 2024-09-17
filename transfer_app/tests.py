import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from transfer_app.models import Transfer
from users.models import User


@pytest.mark.django_db
def test_create_transfer_api():
    """Проверяет создание нового перевода через API."""
    sender = User.objects.create(username='sender')
    recipient = User.objects.create(username='recipient')
    client = APIClient()
    data = {
        "sender": sender.pk,
        "recipient": recipient.pk,
        "amount": 100.00,
        "currency": "RUB",
        "description": "Тестовый перевод",
    }
    response = client.post(reverse('transfer-list'), data, format='json')
    assert response.status_code == 201
    assert response.data['amount'] == 100.00
    assert response.data['currency'] == "RUB"
    assert response.data['description'] == "Тестовый перевод"
    assert Transfer.objects.count() == 1


@pytest.mark.django_db
def test_list_transfers_api():
    """Проверяет получение списка всех переводов через API."""
    sender = User.objects.create(username='sender')
    recipient = User.objects.create(username='recipient')
    Transfer.objects.create(
        sender=sender,
        recipient=recipient,
        amount=100.00,
        currency="RUB",
        description="Тестовый перевод",
    )
    client = APIClient()
    response = client.get(reverse('transfer-list'))
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_retrieve_transfer_api():
    """Проверяет получение информации о конкретном переводе через API."""
    sender = User.objects.create(username='sender')
    recipient = User.objects.create(username='recipient')
    transfer = Transfer.objects.create(
        sender=sender,
        recipient=recipient,
        amount=100.00,
        currency="RUB",
        description="Тестовый перевод",
    )
    client = APIClient()
    response = client.get(reverse('transfer-detail', args=[transfer.pk]))
    assert response.status_code == 200
    assert response.data['amount'] == 100.00
    assert response.data['description'] == "Тестовый перевод"


@pytest.mark.django_db
def test_update_transfer_api():
    """Проверяет обновление информации о переводе через API."""
    sender = User.objects.create(username='sender')
    recipient = User.objects.create(username='recipient')
    transfer = Transfer.objects.create(
        sender=sender,
        recipient=recipient,
        amount=100.00,
        currency="RUB",
        description="Тестовый перевод",
    )
    client = APIClient()
    data = {
        "amount": 200.00,
        "description": "Обновленный перевод",
    }
    response = client.put(reverse('transfer-detail', args=[transfer.pk]), data, format='json')
    assert response.status_code == 200
    assert response.data['amount'] == 200.00
    assert response.data['description'] == "Обновленный перевод"


@pytest.mark.django_db
def test_delete_transfer_api():
    """Проверяет удаление перевода через API."""
    sender = User.objects.create(username='sender')
    recipient = User.objects.create(username='recipient')
    transfer = Transfer.objects.create(
        sender=sender,
        recipient=recipient,
        amount=100.00,
        currency="RUB",
        description="Тестовый перевод",
    )
    client = APIClient()
    response = client.delete(reverse('transfer-detail', args=[transfer.pk]))
    assert response.status_code == 204
    assert Transfer.objects.count() == 0
