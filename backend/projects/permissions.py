from rest_framework import permissions

class IsOwnerProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        if request.user.is_staff:
            return True
        return False
        
class IsMemberProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.members.all()
    
class IsMemberTodoProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.project.members.all()
    
class IsOwnerTodoProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.project.owner == request.user:
            return True
        if request.user.is_staff:
            return True
        return False


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff