from django.db import models
from django.core.validators import MaxLengthValidator
from django.core.exceptions import ValidationError

from product.models import Product


class NetworkElement(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Дистрибьютор'),
        (2, 'Дилерский центр'),
        (3, 'Крупная розничная сеть'),
        (4, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(validators=[MaxLengthValidator(50)], verbose_name="Название")
    email = models.EmailField(verbose_name="Электронная почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(verbose_name="Номер дома")  
    products = models.ManyToManyField(Product, verbose_name="Продукты", blank=True)
    supplier = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='clients', verbose_name="Поставщик")
    debit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Задолженность перед поставщиком")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def get_hierarchy_level(self):
        level = 0
        supplier = self.supplier
        while supplier:
            level += 1
            supplier = supplier.supplier
        return level

    def clean(self):
        if self.supplier == self:
            raise ValidationError("Элемент сети не может быть своим собственным поставщиком.")

    def __str__(self):
        return self.name
