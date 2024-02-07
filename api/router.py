from rest_framework import routers
from .views import CourseViewSet


router = routers.DefaultRouter()
router.register(r'courses-api', CourseViewSet)