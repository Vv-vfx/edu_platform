from django.contrib import admin

from mainapp.models import CourseCategory, Course
from userapp.models import Role, MyUser


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'show_categories')


admin.site.register(Course, CourseAdmin)

admin.site.register(CourseCategory)
admin.site.register(Role)
admin.site.register(MyUser)
