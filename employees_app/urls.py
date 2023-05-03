from django.urls import path
from . views import (
    UserCreateAPIView,
    UserRetrieveAPIView,
    UserListAPIView,
    OrganizationsCreateAPIView,
)

urlpatterns = [
    path('registration/', UserCreateAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('users/<int:id>/', UserRetrieveAPIView.as_view()),
    path('organizations/', OrganizationsCreateAPIView.as_view()),
]
