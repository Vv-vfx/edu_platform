from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  TemplateView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,
                                  FormView)
from rest_framework.authtoken.models import Token

from mainapp.models import CourseCategory, Course
from mainapp.forms import CourseForm, ContactForm
from mainapp.tasks import send_email_to_user, send_email_to_admin
from userapp.models import MyUser
from userapp.user_group_mixins import (
    RegistredRoleGroupRequiredMixin,
    StudentRoleGroupRequiredMixin,
    TeacherRoleGroupRequiredMixin,
    СuratorRoleGroupRequiredMixin
)


class IndexView(ListView):
    model = Course
    template_name = 'mainapp/index.html'
    context_object_name = 'courses'


class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


class CoursesView(
    ListView
):
    model = Course
    template_name = 'mainapp/courses.html'
    context_object_name = 'courses'


class CourseDetailView(
    PermissionRequiredMixin,
    DetailView
):
    permission_required = 'mainapp.view_course'
    model = Course
    template_name = 'mainapp/course.html'
    context_object_name = 'course'

    def handle_no_permission(self):
        # просто перенаправление на другую страницу при отказе в доступе
        # return redirect('userapp:login')  # например, redirect('login')
        print(self.request.get_full_path())

        # перенаправление на страницу login и возврат после успешного входа
        return redirect_to_login(next=self.request.get_full_path(), login_url='userapp:login')


class CourseUpdateView(
    PermissionRequiredMixin,
    UpdateView,
):
    permission_required = 'mainapp.change_course'
    fields = '__all__'
    model = Course
    template_name = 'mainapp/update_course.html'
    success_url = reverse_lazy('mainapp:courses')

    def handle_no_permission(self):
        # просто перенаправление на другую страницу при отказе в доступе
        # return redirect('userapp:login')  # например, redirect('login')
        print(self.request.get_full_path())

        # перенаправление на страницу login и возврат после успешного входа
        return redirect_to_login(next=self.request.get_full_path(), login_url='userapp:login')


class CourseDeleteView(
    PermissionRequiredMixin,
    DeleteView
):
    permission_required = 'mainapp.delete_course'
    model = Course
    template_name = 'mainapp/delete_course.html'
    success_url = reverse_lazy('mainapp:courses')
    context_object_name = 'course'

    def handle_no_permission(self):
        # просто перенаправление на другую страницу при отказе в доступе
        # return redirect('userapp:login')  # например, redirect('login')
        print(self.request.get_full_path())

        # перенаправление на страницу login и возврат после успешного входа
        return redirect_to_login(next=self.request.get_full_path(), login_url='userapp:login')


class CourseAddView(
    PermissionRequiredMixin,
    CreateView
):
    permission_required = 'mainapp.add_course'
    form_class = CourseForm
    model = Course
    template_name = 'mainapp/add_course.html'
    success_url = reverse_lazy('mainapp:courses')

    def handle_no_permission(self):
        # просто перенаправление на другую страницу при отказе в доступе
        # return redirect('userapp:login')  # например, redirect('login')
        print(self.request.get_full_path())

        # перенаправление на страницу login и возврат после успешного входа
        return redirect_to_login(next=self.request.get_full_path(), login_url='userapp:login')


# КАТЕГОРИИ КУРСОВ
class CourseCategoriesView(ListView):
    model = CourseCategory
    context_object_name = 'course_categories'
    template_name = 'mainapp/course_categories.html'
    ordering = ['pk']


class CourseCategoryAddView(
    # TeacherRoleGroupRequiredMixin,
    CreateView
):
    fields = '__all__'
    model = CourseCategory
    template_name = 'mainapp/add_category.html'
    success_url = reverse_lazy('mainapp:course_categories')


class CourseCategoryUpdateView(
    # TeacherRoleGroupRequiredMixin,
    UpdateView
):
    fields = '__all__'
    model = CourseCategory
    template_name = 'mainapp/update_category.html'
    success_url = reverse_lazy('mainapp:course_categories')


class CourseCategoryDeleteView(
    # СuratorRoleGroupRequiredMixin,
    DeleteView
):
    model = CourseCategory
    template_name = 'mainapp/delete_category.html'
    success_url = reverse_lazy('mainapp:course_categories')
    context_object_name = 'category'


class CourseCategoryDetailView(
    # RegistredRoleGroupRequiredMixin,
    # StudentRoleGroupRequiredMixin,
    # TeacherRoleGroupRequiredMixin,
    DetailView
):
    model = CourseCategory
    template_name = 'mainapp/category.html'
    context_object_name = 'category'


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('mainapp:index')
    template_name = 'mainapp/contact.html'

    def form_valid(self, form):
        data = form.cleaned_data
        user_email = data['email']
        message = data['message']
        # print(email, message)
        send_email_to_user.delay(email=user_email,
                                 topic='Вы отправили нам сообщение со следующим содержанием:',
                                 message=message,
                                 )
        send_email_to_admin.delay(email=user_email,
                                  topic='Нам новое сообщение с формы контактов',
                                  message=message,
                                  )

        return super().form_valid(form)


class UsersInfoView(
    СuratorRoleGroupRequiredMixin,
    ListView
):
    model = MyUser
    template_name = 'mainapp/users_info.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.select_related('role')
        queryset = queryset.prefetch_related('courses')

        return queryset


class FetchRequest(TemplateView):
    template_name = 'mainapp/fetch_request.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Проверяем, аутентифицирован ли пользователь
        user = self.request.user
        if user.is_authenticated:
            # Получаем или создаем токен для пользователя
            token = Token.objects.get(user=user)
            context['auth_token'] = token
        else:
            context['auth_token'] = 'Пользователь не аутентифицирован'

        return context

class AxiosRequest(TemplateView):
    template_name = 'mainapp/axios_request.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Проверяем, аутентифицирован ли пользователь
        user = self.request.user
        if user.is_authenticated:
            # Получаем или создаем токен для пользователя
            token = Token.objects.get(user=user)
            context['auth_token'] = token
        else:
            context['auth_token'] = 'Пользователь не аутентифицирован'

        return context


