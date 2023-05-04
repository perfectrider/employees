from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import CustomUser, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    employers = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'employers')

    def get_employers(self, obj):
        employers = obj.customuser_set.values_list('email', flat=True)
        return employers


class ListCreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'phone',
            'organizations',
            'image',
        )
        read_only_fields = ('organizations',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return super().create(validated_data)


class CustomUserSerializer(serializers.ModelSerializer):
    organizations = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Organization.objects.all()
    )

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'phone',
            'organizations',
            'image',
        )
        read_only_fields = ('id',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['organizations'] = list(
            instance.organizations.values_list('name', flat=True))
        return representation
