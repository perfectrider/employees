import pytest
from rest_framework.test import APIClient
from rest_framework.reverse import reverse

from employees_app.models import CustomUser, Organization


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def registration_url():
    return reverse("registration")


@pytest.fixture
def organizations_url():
    return reverse("organizations")


@pytest.fixture
def user():
    user_obj = CustomUser.objects.create(
        email='user@user.com',
        password='1234qwer',
        first_name='Username',
        last_name='Usersurname',
        phone='711111111',
    )

    return user_obj

@pytest.fixture
def organization_1():
    organization_obj = Organization.objects.create(
        name='Alfa',
        description='Red bank',
    )

    return organization_obj

@pytest.fixture
def organization_2():
    organization_obj = Organization.objects.create(
        name='Tinek',
        description='Yeloow bank',
    )

    return organization_obj

@pytest.fixture
def auth_client(user, api_client):
    user = CustomUser.objects.get(email='user@user.com')
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def payload():
    payload = {
        "email": "user@user.com",
        "password": "1234qwer",
        "first_name": "Testname",
        "last_name": "Testsurname",
    }

    return payload


@pytest.fixture
def invalid_payload():
    payload = {
        "email": "user@user.com",
        "password": "",
    }

    return payload
