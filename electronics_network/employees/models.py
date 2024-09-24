from django.db import models
from django.contrib.auth.models import AbstractUser

from network.models import NetworkElement


class Employee(AbstractUser):
    position = models.CharField(max_length=100, verbose_name="Должность", blank=True)
    network_element = models.ForeignKey(NetworkElement, on_delete=models.CASCADE, related_name='employees',
                                        verbose_name="Элемент сети", null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.position} ({'Активен' if self.is_active else 'Неактивен'})"
