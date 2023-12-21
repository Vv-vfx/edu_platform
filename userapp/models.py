from django.db import models
from django.contrib.auth.models import AbstractUser

from mainapp.models import Course


class Role(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    lastname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=1)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname} {self.role}"
