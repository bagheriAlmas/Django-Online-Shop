import os
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('users/avatars/', filename)


class CustomUser(AbstractUser):
    USER_GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    phone = models.BigIntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    postal_code = models.BigIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=USER_GENDER, default='male')
    avatar = models.ImageField(upload_to=get_file_path, default='default_avatar.png', blank=True, null=True)

    def __str__(self):
        return self.username
