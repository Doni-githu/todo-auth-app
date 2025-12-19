from rest_framework import permissions

class IsOwnerProject(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff
    
class IsAuthenticatedOrNot(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.method == "POST":
            return False
        return True