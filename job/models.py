from django.conf import settings
from core.models import User
from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Locations'
    
    def __str__(self):
        return self.name

class Job(models.Model):
    category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='jobs', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_description = models.TextField(blank=True, null=True)
    company_logo = models.ImageField(upload_to='job_images', blank=True, null=True)
    is_filled = models.BooleanField(default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.job_title