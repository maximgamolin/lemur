from django.contrib.auth.models import AbstractUser
from django.db import models

from core.consts import SchemaBlockCategory, SchemaBlockType
from stock.consts import DatasetPriceCurrency


class User(AbstractUser):
    pass


class UserPayment(models.Model):

    user = models.OneToOneField('core.User', on_delete=models.CASCADE, related_name='bill')
    amount = models.DecimalField(max_digits=19, decimal_places=4)
    currency = models.PositiveSmallIntegerField(
        choices=DatasetPriceCurrency.choices(),
        default=DatasetPriceCurrency.RUB.value
    )


class SchemaBlock(models.Model):
    # {id: 1, category: 'Математика', name: 'sum', title: 'Сложение', inPorts: ['a', 'b'], outPorts: ['res']},
    category = models.PositiveSmallIntegerField(choices=SchemaBlockCategory.choices())
    type = models.PositiveSmallIntegerField(choices=SchemaBlockType.choices())
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    in_ports = models.JSONField(null=True)
    out_ports = models.JSONField(blank=True)


# class UserPaymentTransaction(models.Model):
#     pass