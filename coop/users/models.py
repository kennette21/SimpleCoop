from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_producer = models.BooleanField(default=False)
    # add additional fields in here
