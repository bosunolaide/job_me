from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    is_applicant = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    contact_title = models.CharField(max_length=100)
    contact_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_attended = models.BooleanField(default=False)