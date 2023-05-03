from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    organizations = models.ManyToManyField(Organization, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BaseUserManager()

    def __str__(self):
        return self.email


