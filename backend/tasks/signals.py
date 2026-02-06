from django.db.models import Sum
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from projects.models import Project
from tasks.models import Task


def _calculate_hours(start_date, completion_date) -> int:
    if not start_date or not completion_date:
        return 0
    delta_days = (completion_date - start_date).days
    return max(delta_days, 0) * 24


@receiver(pre_save, sender=Task)
def set_task_hours_consumed(sender, instance: Task, **kwargs) -> None:
    previous_status = None
    if instance.pk:
        previous_status = (
            Task.objects.filter(pk=instance.pk).values_list("status", flat=True).first()
        )
    if instance.status == Task.Status.COMPLETED and previous_status != Task.Status.COMPLETED:
        completion_date = timezone.now().date()
        instance.hours_consumed = _calculate_hours(instance.start_date, completion_date)


def _update_project_hours(project_id: int) -> None:
    total = Task.objects.filter(project_id=project_id).aggregate(sum=Sum("hours_consumed"))["sum"]
    Project.objects.filter(pk=project_id).update(hours_consumed=total or 0)


@receiver(post_save, sender=Task)
def update_project_hours_on_save(sender, instance: Task, **kwargs) -> None:
    if instance.project_id:
        _update_project_hours(instance.project_id)


@receiver(post_delete, sender=Task)
def update_project_hours_on_delete(sender, instance: Task, **kwargs) -> None:
    if instance.project_id:
        _update_project_hours(instance.project_id)
