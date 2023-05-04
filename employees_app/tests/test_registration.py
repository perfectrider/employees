import pytest
from rest_framework import status


@pytest.mark.django_db
def test_registration(api_client, registration_url, payload):
    response = api_client.post(
        registration_url,
        data=payload,
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['email'] == payload['email']
    assert response.data['first_name'] == payload['first_name']
    assert response.data['last_name'] == payload['last_name']


@pytest.mark.django_db
def test_invalid_registration(api_client, registration_url, invalid_payload):
    response = api_client.post(
        registration_url,
        data=invalid_payload,
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
