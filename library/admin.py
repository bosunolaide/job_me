from django.contrib import admin
from .models import Library, Category, Location

# Register your models here.

admin.site.register(Library)
admin.site.register(Category)
admin.site.register(Location)

