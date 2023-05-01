from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . views import CustomUserCreateAPIView

urlpatterns = [
    path('registration/', CustomUserCreateAPIView.as_view())
]