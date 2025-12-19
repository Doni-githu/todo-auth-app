from django.contrib import admin
from .models import Todo, Project

admin.site.register([Todo, Project])


# Register your models here.
