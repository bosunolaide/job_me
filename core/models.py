from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)
    is_applicant = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)


class Contact(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=80)
    email_address = models.EmailField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_attended = models.BooleanField(default=False)