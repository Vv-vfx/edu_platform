import random

from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from rest_framework.authtoken.models import Token

from mainapp.models import CourseCategory, Course
from userapp.models import Role, MyUser
from django.contrib.auth.models import Group, Permission

from userapp.user_group import registered_role_group, student_role_group, teacher_role_group, curator_role_group


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
        course_category_list = []
        for category, data in course_categories_dict.items():
            obj = CourseCategory(slug=category, name=data[0], tag=data[1], description=data[2])
            course_category_list.append(obj)

        CourseCategory.objects.bulk_create(course_category_list)

        course_dict = {
            'ios_dev_pro_1': (
                'iOS Developer. Professional',
                'Изучите актуальный стек технологий для современного iOS-разработчика: SwiftUI, Protocol Oriented Programming, Actor и async/await, CoreML, ARKit и RealityKit и др.',
                10000,
                (course_category_list[0], course_category_list[1])
            ),
            'python_developer': (
                'Python Developer',
                'Научитесь программировать на Python',
                20000,
                (course_category_list[0], course_category_list[2])
            ),
            'c_sharp_dev': (
                'C# Developer',
                'Для C-разработчиков с опытом от 2-3 лет, которые хотят углубиться в создание web-приложений, стать fullstack-специалистами.',
                15000,
                (course_category_list[0],)
            ),
            'node_js_dev': (
                'Node.js Developer',
                'Курс рассчитан на frontend-разработчиков или backend-разработчиков со знанием Javascript.',
                9900,
                (course_category_list[0], course_category_list[3],)
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
        role_list = [Role(name=name_role) for name_role in ('registered', 'student', 'teacher')]
        # role_list = [registered, student, teacher]
        Role.objects.bulk_create(role_list)

        # ==================================================
        # ==================================================


        print("Creating User")

        Faker.seed(11)
        fake = Faker('ru_RU')

        for index, _ in enumerate(range(50)):
            Faker.seed(100)
            full_name = fake.unique.name().split()

            role = random.choice(role_list)
            if role.name != 'registered':
                course = random.choice(course_list)
            else:
                course = None

            user = MyUser.objects.create_user(
                username=fake.profile()['username'] + str(index),
                last_name=full_name[0],
                first_name=full_name[1],
                email=fake.unique.email(),
                role=role,
                password=fake.password(length=20)
            )

            if course is not None:
                user.courses.add(course)
                user.save()

            # создаем для пользователя токен для DRF
            Token.objects.create(user=user)

            # добавляем пользователя в группу
            if user.role.name == 'registered':
                registered_role_group.user_set.add(user)
            elif user.role.name == 'student':
                student_role_group.user_set.add(user)
            elif user.role.name == 'teacher':
                teacher_role_group.user_set.add(user)

        print('Создание определенных пользователей для тестов')

        # ======================================
        # создаем пользователя в группе "student"
        user = MyUser.objects.create_user(
            username='student',
            last_name='Ivanov',
            first_name='Ivan',
            email='student@gmail.com',
            # добавляем роль student
            role=role_list[1],
            password='12345'
        )



        # Добавляем в группу Django для "student"
        student_role_group.user_set.add(user)
        # создаем для пользователя токен для DRF
        Token.objects.create(user=user)

        print('user_groups:')
        groups = user.groups.all()
        for group in groups:
            print(group.name)

        print('user_permissions:')
        permissions = user.user_permissions.all()
        for perm in permissions:
            print(perm.codename)



        # ======================================
        # создаем пользователя в группе "teacher"

        user = MyUser.objects.create_user(
            username='teacher',
            last_name='Sergeev',
            first_name='Sergey',
            email='teacher@gmail.com',
            # добавляем роль teacher
            role=role_list[2],
            password='12345'
        )
        # Добавляем в группу Django для "teacher"
        teacher_role_group.user_set.add(user)
        # создаем для пользователя токен для DRF
        Token.objects.create(user=user)

        # ======================================
        # создаем пользователя в группе "curator"

        user = MyUser.objects.create_user(
            username='curator',
            last_name='Sergeev',
            first_name='Sergey',
            email='curator@gmail.com',
            # добавляем роль teacher
            role=role_list[2],
            password='12345'
        )
        # Добавляем в группу Django для "curator"
        curator_role_group.user_set.add(user)
        # создаем для пользователя токен для DRF
        Token.objects.create(user=user)

        self.stdout.write(
            self.style.SUCCESS('Successfully fill db fake'))
