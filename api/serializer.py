from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import Serializer, ModelSerializer, HyperlinkedModelSerializer
from mainapp.models import CourseCategory


class CourseCategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'
