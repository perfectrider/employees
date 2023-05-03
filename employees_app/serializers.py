from .models import CustomUser, Organization
from rest_framework import serializers


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'phone',
            'image',
        )
        read_only_fields = ('id', 'organizations')
        extra_kwargs = {'password': {'write_only': True}}

