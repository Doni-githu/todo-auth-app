from datetime import datetime
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
    
    def save(self,*args , **kwargs):
        if self['status'] == "CONFIRMED":
            self.completed_at = datetime.now()
        return super().save(*args, **kwargs)

    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'id', 'owner')
    
    def validation_name(self, value):
        qs = Project.objects.filter(name__iexact=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError(
                {"name": ["Project with this name already exists."]}
            )
        return value
    
class ProjectWithTodosSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('name', 'id', 'owner', 'todos')

    
    
    def validation_name(self, value):
        qs = Project.objects.filter(name__iexact=value)

        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            raise serializers.ValidationError(
                {"name": ["Project with this name already exists."]}
            )
        return value
    