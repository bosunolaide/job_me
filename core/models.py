from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.managers import UserManager

# Create your models here.

class User(AbstractUser):
    username = None
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_applicant = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()



class Contact(models.Model):
    subject = models.CharField(max_length=100)
    name = models.CharField(max_length=80)
    email_address = models.EmailField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_attended = models.BooleanField(default=False)

    def __unicode__(self):
        return self.subject