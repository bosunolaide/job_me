from django.contrib import admin

from .models import Category, Location, Job

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Job)
