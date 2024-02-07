from rest_framework.viewsets import ModelViewSet
from mainapp.models import CourseCategory
from .serializer import CourseCategorySerializer


class CourseCategoryViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer

