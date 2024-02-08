from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField
from mainapp.models import Course, CourseCategory


class CourseSerializer(HyperlinkedModelSerializer):
    category = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='api:coursecategory-detail',
    )

    class Meta:
        model = Course
        fields = [
            'url',
            'name',
            'description',
            'category'
        ]
        extra_kwargs = {
            'url': {'view_name': 'api:course-detail'}
        }

class CourseCategorySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CourseCategory
        fields = [
            'url',
            'name',
            'description',
        ]
        extra_kwargs = {
            'url': {'view_name': 'api:coursecategory-detail'}
        }