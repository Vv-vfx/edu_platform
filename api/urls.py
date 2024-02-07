from django.urls import path, include
from rest_framework import routers
from api.views import CourseCategoryViewSet

router = routers.DefaultRouter()
router.register(r'coursecategory', CourseCategoryViewSet)

# app_name = 'api'

urlpatterns = [
    path('api/', include(router.urls))
]
