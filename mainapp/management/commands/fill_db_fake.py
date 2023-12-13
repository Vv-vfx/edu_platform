import random

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from mainapp.models import CourseCategory, Course, Role, User


class Command(BaseCommand):
    help = "Fill database with random data"

    def handle(self, *args, **options):
        print("Filling db fake")

        Faker.seed(11)
        fake = Faker('ru_RU')

        # print('Deleting Role')
        # Role.objects.all().delete()

        print("Creating CourseCategory")
        programming = CourseCategory.objects.create(name="Программирование")
        arhitecture = CourseCategory.objects.create(name="Архитектура")
        infrastructure = CourseCategory.objects.create(name="Инфраструктура")
        safety = CourseCategory.objects.create(name="Безопасность")
        gamedev = CourseCategory.objects.create(name="GameDev")

        coursecategory_list = [programming, arhitecture, infrastructure, safety, gamedev]

        print("Creating Course")
        ios_developer = Course.objects.create(name="iOS Developer. Professional",
                                              description='Изучите актуальный стек технологий для современного iOS-разработчика: SwiftUI, Protocol Oriented Programming, Actor и async/await, CoreML, ARKit и RealityKit и др.',
                                              price=10000)

        ios_developer.categories.set((programming, arhitecture))
        ios_developer.save()

        python_developer = Course.objects.create(name="Python Developer",
                                                 description='Научитесь программировать на Python',
                                                 price=20000)
        python_developer.categories.set((programming, safety))
        python_developer.save()
        # c_sharp_developer = Course.objects.create(name="C# Developer",
        #                                           description='Для C-разработчиков с опытом от 2-3 лет, которые хотят углубиться в создание web-приложений, стать fullstack-специалистами.')
        # node_js_developer = Course.objects.create(name="Node.js Developer",
        #                                           description='Курс рассчитан на frontend-разработчиков или backend-разработчиков со знанием Javascript.')
        # course_list = [ios_developer, c_sharp_developer, node_js_developer, python_developer]
        course_list = [ios_developer, python_developer]

        print("Creating Role")
        registered = Role.objects.create(name='registered')
        registered.save()
        student = Role.objects.create(name='student')
        student.save()
        teacher = Role.objects.create(name='teacher')
        teacher.save()

        role_list = [registered, student, teacher]

        print("Creating User")

        user_list = []

        for _ in range(50):
            full_name = fake.name().split()

            role = random.choice(role_list)
            if role is not registered:
                course = random.choice(course_list)
            else:
                course = None

            user = User(lastname=full_name[0],
                        name=full_name[1],
                        surname=full_name[2],
                        email=fake.unique.email(),
                        role=role,
                        password=fake.password(length=20),
                        )
            user.save()
            user.courses.add(course)
            user.save()


        self.stdout.write(
            self.style.SUCCESS('Successfully fill db fake')
        )
