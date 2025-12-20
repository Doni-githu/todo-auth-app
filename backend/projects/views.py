from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsOwnerProject
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CreateAndListProjectAPIView(generics.ListCreateAPIView):
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
        serializer.validation_name(serializer.data.get('name'))
        return super().perform_update(serializer) 