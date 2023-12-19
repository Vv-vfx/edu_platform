from django.contrib import admin

from mainapp.models import CourseCategory, Course, Role, User


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')


admin.site.register(Course, CourseAdmin)

admin.site.register(CourseCategory)
admin.site.register(Role)
admin.site.register(User)
