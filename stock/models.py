from django.db import models
from stock.consts import DatasetStatus, DatasetPriceCurrency


class Dataset(models.Model):

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=255)
    build_description = models.JSONField()
    status = models.PositiveSmallIntegerField(choices=DatasetStatus.choices(), default=DatasetStatus.CREATED.value)
    fields = models.JSONField()
    cached_preview = models.TextField()


class PricingDataset(models.Model):
    dataset = models.OneToOneField('stock.Dataset', on_delete=models.CASCADE)
    is_free = models.BooleanField()
    price = models.DecimalField(max_digits=19, decimal_places=4)
    currency = models.PositiveSmallIntegerField(
        choices=DatasetPriceCurrency.choices(),
        default=DatasetPriceCurrency.RUB.value
    )
