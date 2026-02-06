from django.db import models


class Project(models.Model):
    class Status(models.TextChoices):
        CREATED = "CREATED", "Created"
        IN_PROGRESS = "IN PROGRESS", "In Progress"
        OVERDUE = "OVERDUE", "Overdue"
        COMPLETED = "COMPLETED", "Completed"

    project_name = models.CharField(max_length=255)
    project_description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CREATED)
    hours_consumed = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.project_name
