from rest_framework import serializers
from .models import Project, Todo
from user.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    owner_project = UserSerializer(many=False, read_only=True)
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'owner', 'members', 'owner_project', 'members')

    def validation_name(self, value):
        qs = Project.objects.filter(name__iexact=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)

        if qs.exists():
            raise serializers.ValidationError(
                "Project with this name already exists."
            )
        return value

class TodoSerializer(serializers.ModelSerializer):
    project_obj = ProjectSerializer(many=False, read_only=True)
    
    class Meta:
        model = Todo
        fields = ('name', 'project', 'status', 'project_obj')