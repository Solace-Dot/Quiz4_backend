from django.utils import timezone
from rest_framework import serializers

from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "project_name",
            "project_description",
            "status",
            "hours_consumed",
            "start_date",
            "end_date",
        ]
        read_only_fields = ["status", "hours_consumed"]

    def create(self, validated_data):
        start_date = validated_data.get("start_date")
        today = timezone.now().date()
        status = Project.Status.IN_PROGRESS if start_date == today else Project.Status.CREATED
        return Project.objects.create(status=status, **validated_data)
