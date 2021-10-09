from django.db import models

from market.consts import UserPaymentStatus
from stock.consts import DatasetPriceCurrency


class Collection(models.Model):
    owner = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='collections')


class CollectionItem(models.Model):
    collection = models.ForeignKey('market.Collection', on_delete=models.CASCADE, related_name='collection_items')
    dataset = models.ForeignKey('stock.Dataset', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class UserPurchases(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE)
    dataset = models.ForeignKey('stock.Dataset', on_delete=models.CASCADE, related_name='collection_item')
    price = models.DecimalField(max_digits=19, decimal_places=4)
    currency = models.PositiveSmallIntegerField(
        choices=DatasetPriceCurrency.choices(),
        default=DatasetPriceCurrency.RUB.value
    )
    status = models.PositiveSmallIntegerField(
        choices=UserPaymentStatus.choices(), default=UserPaymentStatus.CREATED.value
    )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
