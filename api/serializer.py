from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField
from mainapp.models import Course


class CourseSerializer(HyperlinkedModelSerializer):
    category = HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='category'
    )

    class Meta:
        model = Course
        fields = ['name', 'description', 'category']
