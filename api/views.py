from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from mainapp.models import Course, CourseCategory
from .group_permission import IsUserCurator, IsUserStudent
from .serializer import CourseSerializer, CourseCategorySerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]
    #
    # def get_permissions(self):
    #     if self.action in ['retrieve', 'list']:
    #         return [IsUserStudent()]
    #     return super().get_permissions()


class CourseCategoryViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.action in ['retrieve', 'list']:
    #         return [IsUserCurator()]
    #     return super().get_permissions()


class UpdateTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Удаляем текущий токен пользователя
        request.user.auth_token.delete()
        # Создаём новый токен
        new_token = Token.objects.create(user=request.user)
        return Response({'new_token': new_token.key}, status.HTTP_200_OK)
