from django.db import models


class CourseCategory(models.Model):
    slug = models.SlugField(unique=True, default='category_slug')
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    tag = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Course(models.Model):
    slug = models.SlugField(unique=True, default='course_slug')
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField(CourseCategory, blank=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    lastname = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    role = models.ForeignKey(Role,on_delete=models.PROTECT, default=1)
    courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname} {self.role}"
