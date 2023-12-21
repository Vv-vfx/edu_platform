from django.core.management.base import BaseCommand

from mainapp.models import CourseCategory, Course, Role, User


class Command(BaseCommand):
    help = "Fill database with random data"

    def handle(self, *args, **options):
        print("Примеры запросов")

        print('*' * 30)
        print('Все курсы')
        print('*' * 30)

        courses = Course.objects.all()
        for course in courses:
            print(course.name)

        print('*' * 30)
        print('Курс с названием "Python Developer"')
        print('*' * 30)

        python_course = Course.objects.filter(name='Python Developer')
        print(python_course.first().name)
        print('*' * 30)

        print('*' * 30)
        print('Курс с стоимостью больше/меньше/равно 14000')
        print('*' * 30)

        # courses = Course.objects.filter(price__gt=14000)
        # courses = Course.objects.filter(price__gte=14000)
        # courses = Course.objects.filter(price__lt=14000)
        courses = Course.objects.filter(price__lte=14000)
        for course in courses:
            print(course.name)

        print('*' * 30)
        print('Курс который содержит "developer" ')
        print('*' * 30)

        courses = Course.objects.filter(name__icontains='developer')
        # courses = Course.objects.filter(name__contains='developer')
        for course in courses:
            print(course.name)

        print('*' * 30)
        print('Курс название категории которого начинается с "Б" ')
        print('*' * 30)

        courses = Course.objects.filter(category__name__startswith='Б')
        # courses = Course.objects.filter(name__contains='developer')
        for course in courses:
            print(course.category.all().values_list('name', flat=True))
            print(course.name)

        print('*' * 30)
        print('Получаем количество курсов через базу')
        print('*' * 30)

        print(courses.count())