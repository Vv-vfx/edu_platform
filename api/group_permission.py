from rest_framework.permissions import BasePermission


class IsUserStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='StudentRoleGroup').exists()


class IsUserCurator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='СuratorRoleGroup').exists()
