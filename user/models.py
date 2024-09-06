from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)
