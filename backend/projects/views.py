from .models import Project, Todo
from .serializers import ProjectSerializer, TodoSerializer
from .permissions import IsMemberTodoProject, IsOwnerProject, IsMemberProject, IsOwnerTodoProject
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework import status

class PostAndListProjectAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.prefetch_related('owner_username').all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff: # type: ignore
            return Project.objects.all()
        return Project.objects.filter(members__in=[user]).all()

    def perform_create(self, serializer):
        serializer.validation_name(serializer.validated_data.get('name'))
        return serializer.save()
    

class RetrieveDeleteAndPutProjectAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.prefetch_related('todos')    
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerProject]
    lookup_field = "id"


    def get_permissions(self):
        self.permission_classes = [IsMemberProject]
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [IsOwnerProject]
        return super().get_permissions()

    def perform_update(self, serializer):
        serializer.validation_name(serializer.validated_data.get('name'))
        return serializer.save() 
    


class PostAndListTodosAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_url_kwarg = "id"
    permission_classes = [IsOwnerProject | IsMemberProject]

    def perform_create(self, serializer):
        serializer.validate_name(serializer.validated_data.get('name'))
        return serializer.save() 


class RetrieveTodoAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    

class RetrieveDeleteAndPutTodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'
    def get_permissions(self):
        self.permission_classes = [IsMemberTodoProject]
        if self.request.method not in SAFE_METHODS:
            print("Ok")
            self.permission_classes = [IsOwnerTodoProject]
        return super().get_permissions()


    def perform_update(self, serializer):   
        serializer.validate_name(serializer.validated_data.get('name'))
        return serializer.save()    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            raise NotFound("Todo not found.")
        if request.user.id != instance.project.owner.id:
            raise PermissionDenied("You do not have permission to delete this todo.")
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)