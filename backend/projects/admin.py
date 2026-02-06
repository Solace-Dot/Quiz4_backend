from django.contrib import admin

from projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "status", "hours_consumed", "start_date", "end_date")
    list_filter = ("status",)
    search_fields = ("project_name",)
