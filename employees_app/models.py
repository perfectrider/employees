from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from PIL import Image

from employees_app.managements.usermanager import CustomUserManager
from employees_app.utils import resize_image, upload_to


class Organization(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    organizations = models.ManyToManyField(Organization,
                                           blank=True,
                                           related_query_name='employers')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            img = resize_image(img)
            self.image = upload_to(self, self.image.name)
            img.save(self.image.path)
        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
