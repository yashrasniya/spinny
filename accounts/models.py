from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    key = models.CharField(max_length=60, blank=True)

    def name(self):
        return f"{self.first_name} {self.last_name}"
