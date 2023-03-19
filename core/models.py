from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_applicant = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)