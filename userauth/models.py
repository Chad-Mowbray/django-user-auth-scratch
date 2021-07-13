from django.db import models
from django.contrib.auth.models import AbstractUser


class BlogUser(AbstractUser):
    is_paid_subscriber = models.BooleanField(default=False)

    class Meta:
        verbose_name = "BlogUser"
        verbose_name_plural = "BlogUsers"