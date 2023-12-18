from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from mainapp.models import CourseCategory, Course


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
    fields = '__all__'
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
