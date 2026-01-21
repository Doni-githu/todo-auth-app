from .models import Project, Todo
from .serializers import ProjectSerializer, ProjectWithTodosSerializer, TodoSerializer
from .permissions import IsMemberTodoProject, IsOwnerProject, IsMemberProject, IsOwnerTodoProject
from rest_framework import generics, views, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework.response import Response



class PostAndListProjectAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
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
    

class DeleteAndPutProjectAPIView(generics.DestroyAPIView, generics.UpdateAPIView):    
    serializer_class = ProjectWithTodosSerializer
    lookup_field = "id"

    def get_queryset(self):
        
        return super().get_queryset()

    def get_permissions(self):
        self.permission_classes = [IsOwnerProject | IsMemberProject]
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [IsOwnerProject]
        return super().get_permissions()

    def perform_update(self, serializer):
        serializer.validation_name(serializer.validated_data.get('name'))
        return serializer.save() 
    
class RetrieveProjectAPIView(views.APIView):
    def get(self, request,id, format=None):
        project = Project.objects.get(id=id)
        todos = Todo.objects.filter(project=int(id))
        serTodos = TodoSerializer(todos, many=True)
        serProject = ProjectSerializer(project)

        return Response({
            'count_of_todos': len(serTodos.data),
            'project': serProject.data,
            'todos': serTodos.data,
        }, status=status.HTTP_200_OK)


class PostAndListTodosAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_url_kwarg = "id"
    permission_classes = [IsOwnerProject | IsMemberProject]

    def perform_create(self, serializer):
        serializer.validate_name(serializer.validated_data.get('name'))
        return serializer.save() 

class RetrieveDeleteAndPutTodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        project = self.kwargs['project_id']
        return Todo.objects.filter(project=project)

    def get_permissions(self):
        self.permission_classes = [IsMemberTodoProject | IsOwnerTodoProject]
        if self.request.method not in SAFE_METHODS:
            self.permission_classes = [IsOwnerTodoProject]
        return super().get_permissions()

    def perform_update(self, serializer):   
        serializer.validate_name(serializer.validated_data.get('name'))
        return serializer.save()    
    def destroy(self, request, *args, **kwargs):
        self.get_permissions()
        return super().destroy(request, *args, **kwargs)