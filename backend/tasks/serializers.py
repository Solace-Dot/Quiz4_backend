from django.utils import timezone
from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "project",
            "task_name",
            "task_description",
            "status",
            "hours_consumed",
            "user_assigned",
            "start_date",
            "end_date",
        ]
        read_only_fields = ["hours_consumed"]

    def create(self, validated_data):
        start_date = validated_data.get("start_date")
        today = timezone.now().date()
        status = Task.Status.IN_PROGRESS if start_date == today else Task.Status.CREATED
        return Task.objects.create(status=status, **validated_data)
