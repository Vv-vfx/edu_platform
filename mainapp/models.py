from django.db import models


class TimeStampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CourseCategory(TimeStampMixin):
    slug = models.SlugField(unique=True, default='category_slug')
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    tag = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Course(TimeStampMixin):
    slug = models.SlugField(unique=True, default='course_slug')
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ManyToManyField(CourseCategory, blank=True)

    def show_categories(self):
        categories = ','.join([i.name for i in self.category.all()])
        return categories

    def __str__(self):
        return self.name





