from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import *
from .models import User

class UserAdmin(UserAdmin):
    # Customize the admin panel for your user model

 admin.site.register(User, UserAdmin)
 admin.site.register(project)
 admin.site.register(task)
 admin.site.register(goal)
 admin.site.register(feedback)

# Register your models here.