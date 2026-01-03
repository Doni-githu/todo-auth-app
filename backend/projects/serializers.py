from os import read
from rest_framework import serializers
from .models import Project, Todo
from user.serializers import UserSerializer


class TodoSerializer(serializers.ModelSerializer):
    assigned = UserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ('id','name', 'project', 'status', 'assigned_to', 'assigned')

    def validate_name(self, value):
        qs = Todo.objects.filter(name__iexact=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError(
                {"name": ["Todo with this name already exists."]}
            )
        return value

class ProjectSerializer(serializers.ModelSerializer):
    # members = UserSerializer(many=True, read_only=True)
    # todos = TodoSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('name', 'id','owner', 'members', 'todos')
    
    def validation_name(self, value):
        qs = Project.objects.filter(name__iexact=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError(
                {"name": ["Project with this name already exists."]}
            )
        return value
    