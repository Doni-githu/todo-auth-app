from rest_framework import permissions

class IsOwnerProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user 

class IsMemberProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.members.all()