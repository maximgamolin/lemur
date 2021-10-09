from django.db import models
from stock.consts import DatasetStatus, DatasetPriceCurrency


class Collection(models.Model):
    owner = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='collections')


class CollectionItem(models.Model):
    collection = models.ForeignKey('market.Collection', on_delete=models.CASCADE, related_name='collection_item')
    dataset = models.ForeignKey('stock.Dataset', on_delete=models.CASCADE)


class UserPurchases(models.Model):
    dataset = models.ForeignKey('stock.Dataset', on_delete=models.CASCADE, related_name='collection_item')
    price = models.DecimalField(max_digits=19, decimal_places=4)
    currency = models.PositiveSmallIntegerField(
        choices=DatasetPriceCurrency.choices(),
        default=DatasetPriceCurrency.RUB.value
    )
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
