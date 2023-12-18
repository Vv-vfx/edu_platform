from django.contrib import admin
from django.urls import path

from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<slug:slug>/', views.CourseCategoryDetailView.as_view(), name='category'),
    path('course_category/update/<slug:slug>', views.CourseCategoryUpdateView.as_view(), name='update_category'),
    path('course_category/delete/<slug:slug>', views.CourseCategoryDeleteView.as_view(), name='delete_category'),
    path('course_category/add', views.CourseCategoryAddView.as_view(), name='add_category'),
    path('course_categories/', views.CourseCategoriesView.as_view(), name='course_categories'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course'),
    path('course/update/<int:pk>', views.CourseUpdateView.as_view(), name='update_course'),
    path('course/delete/<int:pk>', views.CourseDeleteView.as_view(), name='delete_course'),
    path('course/add', views.CourseAddView.as_view(), name='add_course'),
    path('courses/', views.CoursesView.as_view(), name='courses'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
