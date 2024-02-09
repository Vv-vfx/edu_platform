from django.contrib.auth.models import Permission, Group

print("Creating Groups for Django")
# Сначала формируем основные permissions:

model = 'Course'
# for model in ['Course', 'CourseCategory']:  # модели
course_view_permission = Permission.objects.get(codename=f'view_{model.lower()}')
course_add_permission = Permission.objects.get(codename=f'add_{model.lower()}')
course_change_permission = Permission.objects.get(codename=f'change_{model.lower()}')
course_delete_permission = Permission.objects.get(codename=f'delete_{model.lower()}')

model = 'CourseCategory'
course_category_view_permission = Permission.objects.get(codename=f'view_{model.lower()}')
course_category_add_permission = Permission.objects.get(codename=f'add_{model.lower()}')
course_category_change_permission = Permission.objects.get(codename=f'change_{model.lower()}')
course_category_delete_permission = Permission.objects.get(codename=f'delete_{model.lower()}')

# ====================================================

# Создание группы группы прав для роли "registered"
registered_role_group, _ = Group.objects.get_or_create(name='RegistredRoleGroup')
# добавляем permission: только view
registered_role_group.permissions.add(
    course_view_permission,
    course_category_view_permission,
)

# Создание группы группы прав для роли "student"
student_role_group, _ = Group.objects.get_or_create(name='StudentRoleGroup')
# добавляем permission: только view
student_role_group.permissions.add(
    course_view_permission,
    course_category_view_permission,
)

# Создание группы группы прав для роли "teacher"
teacher_role_group, _ = Group.objects.get_or_create(name='TeacherRoleGroup')
# добавляем permission: view, change, add
teacher_role_group.permissions.add(
    course_view_permission,
    course_add_permission,
    course_change_permission,
    course_category_view_permission,
    course_category_add_permission,
    course_category_change_permission,
)

# Создание группы группы прав для роли "curator"
curator_role_group, _ = Group.objects.get_or_create(name='СuratorRoleGroup')
# добавляем permission: view, change, add, delete
curator_role_group.permissions.add(
    course_view_permission,
    course_add_permission,
    course_change_permission,
    course_delete_permission,
    course_category_view_permission,
    course_category_add_permission,
    course_category_change_permission,
    course_category_delete_permission
)
