from rest_framework import permissions

class IsOwnerProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner.id == request.user.id or request.user.is_staff

class IsMemberProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.members.all() or request.user.id  == obj.owner.id
class IsMemberTodoProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.project.members.all()
    
class IsOwnerTodoProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.project.owner.id == request.project.user.id or request.user.is_staff


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff