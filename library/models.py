from django.db import models
from django.conf import settings


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

class Library(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='libraries', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=80)
    job_title = models.CharField(max_length=255)
    curriculum_vitae = models.FileField(upload_to='pdfs_library/')
    category = models.ForeignKey(Category, related_name='libraries', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='libraries', on_delete=models.CASCADE)
    applicant_image = models.ImageField(upload_to='cv_images', blank=True, null=True)
    is_employed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['full_name']
     
    def __str__(self):
        return f"{self.full_name}"
