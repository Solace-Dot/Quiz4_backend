from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskSerializer
from users.permissions import IsAdminOrManager


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrManager]


class TaskUpdateView(generics.UpdateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role in {"ADMIN", "MANAGER"}:
            return Task.objects.all()
        return Task.objects.filter(user_assigned=user)
