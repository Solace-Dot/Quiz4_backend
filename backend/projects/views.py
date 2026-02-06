from rest_framework import generics

from projects.models import Project
from projects.serializers import ProjectSerializer
from users.permissions import IsAdmin


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == "ADMIN":
            return Project.objects.all()
        return Project.objects.filter(tasks__user_assigned=user).distinct()


class ProjectDetailView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == "ADMIN":
            return Project.objects.all()
        return Project.objects.filter(tasks__user_assigned=user).distinct()


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAdmin]
