import pytest
from rest_framework import status


@pytest.mark.django_db
def test_get_all_users_not_admin(
        auth_client,
        users_url,
):
    response = auth_client.get(users_url)

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_get_all_users_admin(
        auth_client_admin,
        users_url,
        admin_user,
        user
):
    response = auth_client_admin.get(users_url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()[0]['email'] == admin_user.email
    assert response.json()[1]['email'] == user.email


@pytest.mark.django_db
def test_get_user_obj(auth_client, user):
    response = auth_client.get(f'/users/{user.id}/')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == user.id


@pytest.mark.django_db
def test_another_user_update_profile(auth_client, user, admin_user):
    payload = {
        "email": user.email,
        "first_name": "new_name"
    }

    response = auth_client.patch(f'/users/{admin_user.id}/', payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_user_set_organizations(
        auth_client,
        user,
        organization_1,
        organization_2
):
    payload = {
        "email": user.email,
        "organizations": [organization_1.name, organization_2.name]
    }

    response = auth_client.patch(f'/users/{user.id}/', payload)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['organizations'][0] == organization_1.name
    assert response.data['organizations'][1] == organization_2.name
