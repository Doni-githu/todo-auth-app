from .models import Project, Todo
from .serializers import ProjectSerializer, TodoSerializer
from .permissions import IsOwnerProject, IsMemberProject
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, SAFE_METHODS
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework import status

class PostAndListProjectAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff: # type: ignore
            return Project.objects.prefetch_related('members').all()
        return Project.objects.filter(members__in=[user]).prefetch_related('members')


    def perform_create(self, serializer):
        serializer.validation_name(serializer.validated_data.get('name'))
        return serializer.save()
    

class RetrieveDeleteAndPutProjectAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerProject]
    lookup_field = "id"


    def perform_update(self, serializer):
        serializer.validate_name(serializer.data.get('name'))
        return serializer.save() 
    


class PostAndListTodosAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_url_kwarg = "id"
    permission_classes = [IsOwnerProject | IsMemberProject]

    def perform_create(self, serializer):
        serializer.validate_name(serializer.validated_data.get('name'))
        return serializer.save() 
class RetrieveDeleteAndPutTodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOwnerProject | IsMemberProject]
    lookup_field = "id"

    def get_queryset(self):
        project_id = self.kwargs.get('id')
        return Todo.objects.filter(project__id=project_id)
    def get_object(self):
        queryset = self.get_queryset()
        todo_id = self.kwargs.get('todo_id')

        try:
            return queryset.get(id=todo_id)
        except Todo.DoesNotExist: 
            raise NotFound("Todo not found.")
    

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