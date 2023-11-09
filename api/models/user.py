# api/managers.py
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, enrolment_no, username, year, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, enrolment_no=enrolment_no, username=username, year=year, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, enrolment_no, username, year, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, enrolment_no, username, year, password, **extra_fields)



class User(AbstractUser):
    email = models.EmailField(unique=True)
    enrolment_no = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=255,unique=True)
    year = models.IntegerField()
    is_member = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "enrolment_no", "year"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
