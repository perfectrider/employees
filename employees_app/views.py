from django.contrib.auth import get_user_model
from rest_framework import generics, status, exceptions
from rest_framework import permissions
from .permissions import IsOwner
from rest_framework.response import Response

from .serializers import (
    CustomUserSerializer, OrganizationSerializer,
    ListCreateUserSerializer
)
from .models import CustomUser, Organization

get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ListCreateUserSerializer
    permission_classes = [permissions.AllowAny]


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserRetrieveAPIView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, id=self.kwargs.get('id'))
        return obj

    def handle_exception(self, exc):
        if isinstance(exc, exceptions.NotFound):
            return Response({'detail': 'Object not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)


class OrganizationsCreateAPIView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticated]
