from .models import Project, User
from .serializers import ProjectSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CreateAndListProjectAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        
        return super().perform_create(serializer)