from django.urls import path
from . views import CustomUserCreateAPIView
from . views import OrganizationsCreateAPIView, UserListAPIView

urlpatterns = [
    path('registration/', CustomUserCreateAPIView.as_view()),
    path('organizations/', OrganizationsCreateAPIView.as_view()),
    path('users/', UserListAPIView.as_view())
]
