import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_organizations(
        auth_client,
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
def test_get_organizations(
        auth_client,
        organizations_url,
        organization_1,
        organization_2,
):
    response = auth_client.get(organizations_url)

    print(response.json()[0]['name'])

    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]['name'] == organization_1.name
    assert response.json()[1]['name'] == organization_2.name

