from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from mainapp.models import Course, CourseCategory
from .serializer import CourseSerializer, CourseCategorySerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser]


class CourseCategoryViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
