from rest_framework import routers
from .views import CourseViewSet, CourseCategoryViewSet

router = routers.DefaultRouter()

router.register(r'course', CourseViewSet)
router.register(r'coursecategory', CourseCategoryViewSet)
