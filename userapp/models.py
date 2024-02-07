from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

from mainapp.models import Course


class Role(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    # lastname = models.CharField(max_length=256)
    # name = models.CharField(max_length=256)
    # surname = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=1)
    courses = models.ManyToManyField(Course, blank=True)


    def save(self, *args, **kwargs):
        # Установка роли по умолчанию, если она не указана

        # Проверяем, cоздается ли новый экземпляр объекта или обновляется существующий
        if self._state.adding and not self.role_id:
            # получаем роль из базы
            default_role = Role.objects.get(name='registered')  # Или get(id=desired_id)
            self.role = default_role
            Token.objects.create(user=self)




        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} {self.email} {self.first_name} {self.last_name} {self.role}"
