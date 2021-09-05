from django.contrib import admin
from .models import Employee,License,Task,Project
# Register your models here.

admin.site.register([Employee,License,Task,Project])