import django_rq
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView, FormView
from mainapp.models import CourseCategory, Course
from mainapp.forms import CourseForm, ContactForm
from mainapp.tasks import send_email_to_user, send_email_to_admin
from userapp.models import MyUser


class IndexView(ListView):
    model = Course
    template_name = 'mainapp/index.html'
    context_object_name = 'courses'


class ContactView(TemplateView):
    template_name = 'mainapp/contact.html'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'mainapp/course.html'
    context_object_name = 'course'


class CourseUpdateView(UpdateView):
    fields = '__all__'
    model = Course
    template_name = 'mainapp/update_course.html'
    success_url = reverse_lazy('mainapp:courses')


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'mainapp/delete_course.html'
    success_url = reverse_lazy('mainapp:courses')
    context_object_name = 'course'


class CourseAddView(CreateView):
    form_class = CourseForm
    model = Course
    template_name = 'mainapp/add_course.html'
    success_url = reverse_lazy('mainapp:courses')


class CoursesView(ListView):
    model = Course
    template_name = 'mainapp/courses.html'
    context_object_name = 'courses'


# КАТЕГОРИИ КУРСОВ
class CourseCategoriesView(ListView):
    model = CourseCategory
    context_object_name = 'course_categories'
    template_name = 'mainapp/course_categories.html'
    ordering = ['pk']


class CourseCategoryAddView(CreateView):
    fields = '__all__'
    model = CourseCategory
    template_name = 'mainapp/add_category.html'
    success_url = reverse_lazy('mainapp:course_categories')


class CourseCategoryUpdateView(UpdateView):
    fields = '__all__'
    model = CourseCategory
    template_name = 'mainapp/update_category.html'
    success_url = reverse_lazy('mainapp:course_categories')


class CourseCategoryDeleteView(DeleteView):
    model = CourseCategory
    template_name = 'mainapp/delete_category.html'
    success_url = reverse_lazy('mainapp:course_categories')
    context_object_name = 'category'


class CourseCategoryDetailView(DetailView):
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


class UsersInfoView(ListView):
    model = MyUser
    template_name = 'mainapp/users_info.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = queryset.select_related('role')
        queryset = queryset.prefetch_related('courses')

        return queryset
