from django.db import models
from user.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner_project")
    members = models.ManyToManyField(User, related_name="members", blank=True)

    def __str__(self):
        return f'Project - {self.name}'
    

class Todo(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        CANCELLED = "CANCELLED", "Cancelled"
    
    name = models.CharField(max_length=255, unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="todos")
    status = models.CharField(
        max_length=15,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )

    def __str__(self) -> str:
        return f'Todo - {self.name} in project - {self.project.name}'
