import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import TeamMember

@pytest.mark.django_db
def test_create_team_member():
    team_member = TeamMember.objects.create(
        name="Иван",
        last_name="Иванов",
        role="Разработчик",
       
    )
    assert team_member.name == "Иван"
    assert team_member.last_name == "Иванов"
    assert team_member.role == "Разработчик"

@pytest.mark.django_db
def test_team_member_str():
    team_member = TeamMember.objects.create(
        name="Иван",
        last_name="Иванов",
        role="Разработчик",
       
    )
    assert str(team_member) == "Иван Иванов - Разработчик"

@pytest.mark.django_db
def test_team_member_list_api():
    client = APIClient()
    response = client.get(reverse('teammember-list'))
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_team_member_api():
    client = APIClient()
    data = {
        "name": "Иван",
        "last_name": "Иванов",
        "role": "Разработчик",
       
    }
    response = client.post(reverse('teammember-list'), data)
    assert response.status_code == 201
    assert response.data['name'] == "Иван"

