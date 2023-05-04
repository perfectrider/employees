import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

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
def users_url():
    return reverse("users")



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
def user(organization_1):
    user_obj = CustomUser.objects.create(
        email='user@user.com',
        password='1234qwer',
        first_name='Username',
        last_name='Usersurname',
        phone='711111111',
    )

    user_obj.organizations.add(organization_1)
    user_obj.save()

    return user_obj


@pytest.fixture
def admin_user():
    user_obj = CustomUser.objects.create(
        email='admin@user.com',
        password='1234qwer',
        first_name='admin',
        last_name='admin',
        is_superuser=True,
        is_staff=True,
    )

    return user_obj


@pytest.fixture
def auth_client(user, api_client):
    user = CustomUser.objects.get(email='user@user.com')
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def auth_client_admin(admin_user, user, api_client):
    user = CustomUser.objects.get(email='admin@user.com')
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
