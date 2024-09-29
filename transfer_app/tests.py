import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from transfer_app.models import Payment
from users.models import User


@pytest.mark.django_db
def test_create_payment_api():
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
    response = client.post(reverse('payment-list'), data, format='json')
    assert response.status_code == 201
    assert response.data['amount'] == 100.00
    assert response.data['currency'] == "RUB"
    assert response.data['description'] == "Тестовый перевод"
    assert Payment.objects.count() == 1


@pytest.mark.django_db
def test_list_payment_api():
    """Проверяет получение списка всех переводов через API."""
    sender = User.objects.create(username='sender')
    recipient = User.objects.create(username='recipient')
    Payment.objects.create(
        sender=sender,
        recipient=recipient,
        amount=100.00,
        currency="RUB",
        description="Тестовый перевод",
    )
    client = APIClient()
    response = client.get(reverse('payment-list'))
    assert response.status_code == 200
    assert len(response.data) == 1


@pytest.mark.django_db
def test_retrieve_payment_api():
    """Проверяет получение информации о конкретном переводе через API."""
    sender = User.objects.create(username='sender')
    recipient = User.objects.create(username='recipient')
    payment = Payment.objects.create(
        sender=sender,
        recipient=recipient,
        amount=100.00,
        currency="RUB",
        description="Тестовый перевод",
    )
    client = APIClient()
    response = client.get(reverse('payment-detail', args=[payment.pk]))
    assert response.status_code == 200
    assert response.data['amount'] == 100.00
    assert response.data['description'] == "Тестовый перевод"


@pytest.mark.django_db
def test_update_payment_api():
    """Проверяет обновление информации о переводе через API."""
    sender = User.objects.create(username='sender')
    recipient = User.objects.create(username='recipient')
    payment = Payment.objects.create(
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
    response = client.put(reverse('payment-detail', args=[payment.pk]), data, format='json')
    assert response.status_code == 200
    assert response.data['amount'] == 200.00
    assert response.data['description'] == "Обновленный перевод"


@pytest.mark.django_db
def test_delete_payment_api():
    """Проверяет удаление перевода через API."""
    sender = User.objects.create(username='sender')
    recipient = User.objects.create(username='recipient')
    payment = Payment.objects.create(
        sender=sender,
        recipient=recipient,
        amount=100.00,
        currency="RUB",
        description="Тестовый перевод",
    )
    client = APIClient()
    response = client.delete(reverse('payment-detail', args=[payment.pk]))
    assert response.status_code == 204
    assert Payment.objects.count() == 0
