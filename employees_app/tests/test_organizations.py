import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_organizations(
        auth_client,
        user,
        organizations_url,
        organization_1,
        organization_2,
):
    response = auth_client.get(organizations_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]['name'] == organization_1.name
    assert response.json()[1]['name'] == organization_2.name
    assert response.json()[0]['description'] == organization_1.description
    assert response.json()[1]['description'] == organization_2.description
    assert response.json()[0]['employers'][0] == user.email

@pytest.mark.django_db
def test_get_organizations_not_auth(
        api_client,
        organizations_url,
        organization_1,
        organization_2,
):
    response = api_client.get(organizations_url)

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_put_organizations(
        auth_client,
        organizations_url,
):
    payload = {
        "name": "Sber",
        "description": "Green Bank",
    }

    response = auth_client.post(organizations_url, payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == payload['name']
    assert response.data['description'] == payload['description']


