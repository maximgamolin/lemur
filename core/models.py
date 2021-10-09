from django.db import models
from django.contrib.auth.models import AbstractUser
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


# class UserPaymentTransaction(models.Model):
#     pass