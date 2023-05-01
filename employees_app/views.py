from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from .serializers import CustomUserSerializer

get_user_model()

class CustomUserCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]
