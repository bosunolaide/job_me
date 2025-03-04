from django.conf import settings
from core.models import User
from django.db import models

from job.models import Job


class Conversation(models.Model):
    job = models.ForeignKey(Job, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)
    
class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    cover_letter = models.TextField()
    curriculum_vitae = models.FileField(upload_to='cv_pdfs/', default="0000.pdf")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_messages', on_delete=models.CASCADE)
