from django.db import models
from django.core.validators import MaxLengthValidator


class Product(models.Model):
    name = models.CharField(validators=[MaxLengthValidator(25)], verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода на рынок")

    def __str__(self):
        return f"{self.name} ({self.model})"
