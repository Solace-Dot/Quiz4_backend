from django.urls import path

from tasks.views import TaskCreateView, TaskUpdateView

urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
]
