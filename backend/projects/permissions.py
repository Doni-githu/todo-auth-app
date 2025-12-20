from rest_framework import permissions

class IsOwnerProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user 

class IsMemberProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.members.all()
    
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff