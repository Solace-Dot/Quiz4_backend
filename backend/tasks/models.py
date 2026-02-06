from django.conf import settings
from django.db import models

from projects.models import Project


class Task(models.Model):
    class Status(models.TextChoices):
        CREATED = "CREATED", "Created"
        IN_PROGRESS = "IN PROGRESS", "In Progress"
        OVERDUE = "OVERDUE", "Overdue"
        COMPLETED = "COMPLETED", "Completed"

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CREATED)
    hours_consumed = models.PositiveIntegerField(default=0)
    user_assigned = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.task_name
