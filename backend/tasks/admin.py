from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_name", "project", "status", "hours_consumed", "start_date", "end_date")
    list_filter = ("status", "project")
    search_fields = ("task_name",)
