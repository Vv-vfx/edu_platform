from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField
from mainapp.models import Course, CourseCategory


class CourseSerializer(HyperlinkedModelSerializer):
    category = HyperlinkedRelatedField(
        many=True,
        view_name='api:coursecategory-detail',
        queryset=CourseCategory.objects.all()

    )

    class Meta:
        model = Course
        fields = [
            'url',
            'name',
            'price',
            'description',
            'category'
        ]
        extra_kwargs = {
            'url': {'view_name': 'api:course-detail'}
        }

    def create(self, validated_data):
        print('зашли в create-api')
        print(validated_data)
        # Извлечение категорий из валидированных данных
        categories_data = validated_data.pop('category', [])

        # Создание экземпляра курса
        course = Course.objects.create(**validated_data)

        # Добавление категорий к курсу
        for category in categories_data:
            course.category.add(category)

        return coursent(validated_data)
        # Извлечение категорий из валидированных данных
        categories_data = validated_data.pop('category', [])

        # Создание экземпляра курса
        course = Course.objects.create(**validated_data)

        # Добавление категорий к курсу
        for category in categories_data:
            course.category.add(category)

        return course




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