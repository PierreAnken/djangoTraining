from django.contrib import admin

# Register your models here.
from .models import Project

# add the model into the admin panel
admin.site.register(Project)
