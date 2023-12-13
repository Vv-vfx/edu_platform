from django.contrib import admin

from mainapp.models import CourseCategory, Course, Role, User

# Register your models here.
admin.site.register(CourseCategory)
admin.site.register(Course)
admin.site.register(Role)
admin.site.register(User)
