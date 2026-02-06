from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomerUser(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        USER = "USER", "User"

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USER)

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"
