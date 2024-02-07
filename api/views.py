from rest_framework.viewsets import ModelViewSet
from mainapp.models import CourseCategory
from .serializer import CourseSerializer


class CourseViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseSerializer

