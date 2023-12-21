import random

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from mainapp.models import CourseCategory, Course
from userapp.models import Role, MyUser


class Command(BaseCommand):
    help = "Fill database with random data"

    def handle(self, *args, **options):
        print("Filling db fake")



        # print('Deleting Role')
        # Role.objects.all().delete()

        print("Creating CourseCategory")
        course_categories_dict = {
            "programming": (
                'Программирование',
                '#универсально',
                'Узнайте языки программирования и основы разработки ПО, от начального до продвинутого уровня, включая практические задания и проекты.',
            ),
            'arhitecture': (
                'Архитектура',
                '#перспективно',
                "Изучите принципы проектирования и строительства, включая историю архитектуры, современные технологии и устойчивое развитие.",

            ),
            'infrastructure': (
                'Инфраструктура',
                '#интересно',
                'Курсы, посвященные основам сетевой инфраструктуры, облачным технологиям и управлению данными в информационных системах.',

            ),
            'safety': (
                'Безопасность',
                '#высокий спрос',
                'Изучение методов защиты информационных систем, кибербезопасности и превентивных мер по обеспечению безопасности данных и приложений.',

            ),
            'gamedev': (
                'GameDev',
                '#захватывающе',
                'Обучение разработке игр, включая программирование, дизайн, анимацию и управление проектами в индустрии видеоигр.',

            ),
            'administration': (
                'Администрирование',
                '#стабильно',
                'Курсы по администрированию систем, сетей и баз данных, включая управление серверами и обеспечение стабильной работы ИТ-инфраструктуры.',
            ),
        }
        coursecategory_list = []
        for category, data in course_categories_dict.items():
            obj = CourseCategory.objects.create(slug=category, name=data[0], tag=data[1], description=data[2])
            obj.save()
            coursecategory_list.append(obj)

        # coursecategory_list = [programming, arhitecture, infrastructure, safety, gamedev, administration]

        course_dict = {
            'ios_dev_pro_1': (
                'iOS Developer. Professional',
                'Изучите актуальный стек технологий для современного iOS-разработчика: SwiftUI, Protocol Oriented Programming, Actor и async/await, CoreML, ARKit и RealityKit и др.',
                10000,
                (coursecategory_list[0], coursecategory_list[1])
            ),
            'python_developer': (
                'Python Developer',
                'Научитесь программировать на Python',
                20000,
                (coursecategory_list[0], coursecategory_list[2])
            ),
            'c_sharp_dev': (
                'C# Developer',
                'Для C-разработчиков с опытом от 2-3 лет, которые хотят углубиться в создание web-приложений, стать fullstack-специалистами.',
                15000,
                (coursecategory_list[0],)
            ),
            'node_js_dev': (
                'Node.js Developer',
                'Курс рассчитан на frontend-разработчиков или backend-разработчиков со знанием Javascript.',
                9900,
                (coursecategory_list[0], coursecategory_list[3],)
            ),
        }

        print("Creating Course")
        course_list = []
        for course, data in course_dict.items():
            obj = Course.objects.create(slug=course, name=data[0], description=data[1], price=data[2])
            obj.category.set(data[3])
            obj.save()
            course_list.append(obj)

        # course_list = [ios_developer, c_sharp_developer, node_js_developer, python_developer]

        print("Creating Role")
        registered = Role.objects.create(name='registered')
        registered.save()
        student = Role.objects.create(name='student')
        student.save()
        teacher = Role.objects.create(name='teacher')
        teacher.save()

        role_list = [registered, student, teacher]

        print("Creating User")

        Faker.seed(11)
        fake = Faker('ru_RU')

        for index, _ in enumerate(range(10)):
            Faker.seed(100)
            full_name = fake.unique.name().split()
            # print(full_name)

            role = random.choice(role_list)
            if role is not registered:
                course = random.choice(course_list)
            else:
                course = None

            user = MyUser(
                        username=fake.profile()['username'] + str(index),
                        lastname=full_name[0],

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
            self.style.SUCCESS('Successfully fill db fake'))
