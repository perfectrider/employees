from django.urls import path

from .views import (OrganizationsCreateAPIView, UserCreateAPIView,
                    UserListAPIView, UserRetrieveAPIView)

urlpatterns = [
    path('registration/', UserCreateAPIView.as_view(),
         name='registration'),
    path('users/', UserListAPIView.as_view()),
    path('users/<int:id>/', UserRetrieveAPIView.as_view()),
    path('organizations/', OrganizationsCreateAPIView.as_view(),
         name='organizations'),
]
