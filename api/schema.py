import graphene
from graphene_django import DjangoObjectType

from mainapp.models import Course
from userapp.models import MyUser


class UserType(DjangoObjectType):
    class Meta:
        model = MyUser
        fields = '__all__'


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = '__all__'

class Query(graphene.ObjectType):
    users_list = graphene.List(UserType)
    courses_list = graphene.List(CourseType)

    def resolve_users_list(self, info):
        return MyUser.objects.all()

    def resolve_courses_list(self, info):
        return Course.objects.all()


schema = graphene.Schema(query=Query)
