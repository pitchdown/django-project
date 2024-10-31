from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    last_active_datetime = models.DateTimeField(default=timezone.now)
    pass