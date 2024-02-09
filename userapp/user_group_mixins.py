from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse


class RegistredRoleGroupRequiredMixin(UserPassesTestMixin):
    group_required = "RegistredRoleGroup"  # Название вашей группы

    def test_func(self):
        user = self.request.user
        print(user.groups.filter(name=self.group_required).exists())
        return user.groups.filter(name=self.group_required).exists()

    def handle_no_permission(self):
        # просто перенаправление на другую страницу при отказе в доступе
        # return redirect('userapp:login')  # например, redirect('login')

        # перенаправление на страницу login и возврат после успешного входа
        login_url = reverse('userapp:login')
        return redirect_to_login(next=self.request.get_full_path(), login_url=login_url)

class StudentRoleGroupRequiredMixin(UserPassesTestMixin):
    group_required = "StudentRoleGroup"  # Название вашей группы

    def test_func(self):
        user = self.request.user
        print(user.groups.filter(name=self.group_required).exists())
        return user.groups.filter(name=self.group_required).exists()

    def handle_no_permission(self):
        # просто перенаправление на другую страницу при отказе в доступе
        # return redirect('userapp:login')  # например, redirect('login')

        # перенаправление на страницу login и возврат после успешного входа
        login_url = reverse('userapp:login')
        return redirect_to_login(next=self.request.get_full_path(), login_url=login_url)

class TeacherRoleGroupRequiredMixin(UserPassesTestMixin):
    group_required = "TeacherRoleGroup"  # Название вашей группы

    def test_func(self):
        user = self.request.user
        print(user.groups.filter(name=self.group_required).exists())
        return user.groups.filter(name=self.group_required).exists()

    def handle_no_permission(self):
        # просто перенаправление на другую страницу при отказе в доступе
        # return redirect('userapp:login')  # например, redirect('login')

        # перенаправление на страницу login и возврат после успешного входа
        login_url = reverse('userapp:login')
        return redirect_to_login(next=self.request.get_full_path(), login_url=login_url)

class СuratorRoleGroupRequiredMixin(UserPassesTestMixin):
    group_required = "СuratorRoleGroup"  # Название вашей группы

    def test_func(self):
        user = self.request.user
        print(user.groups.filter(name=self.group_required).exists())
        return user.groups.filter(name=self.group_required).exists()

    def handle_no_permission(self):
        # просто перенаправление на другую страницу при отказе в доступе
        # return redirect('userapp:login')  # например, redirect('login')

        # перенаправление на страницу login и возврат после успешного входа
        login_url = reverse('userapp:login')
        return redirect_to_login(next=self.request.get_full_path(), login_url=login_url)
