from django.db import models

from stock.consts import DatasetStatus, DatasetPriceCurrency, PermissionsType


class Dataset(models.Model):

    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_id = models.CharField(max_length=255)
    build_description = models.JSONField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=DatasetStatus.choices(), default=DatasetStatus.CREATED.value)
    fields = models.JSONField(null=True, blank=True)
    cached_preview = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Dataset {self.id} - {self.name}"


class DatasetPermissions(models.Model):
    dataset = models.OneToOneField('stock.Dataset', on_delete=models.CASCADE, related_name='perms')
    is_public = models.BooleanField(default=True)
    users = models.ManyToManyField('core.User', blank=True)
    type = models.PositiveSmallIntegerField(choices=PermissionsType.choices(), default=PermissionsType.ONLY.value)


class PricingDataset(models.Model):
    dataset = models.OneToOneField('stock.Dataset', on_delete=models.CASCADE, related_name='pricing')
    is_free = models.BooleanField()
    price = models.DecimalField(max_digits=19, decimal_places=4, default=0)
    currency = models.PositiveSmallIntegerField(
        choices=DatasetPriceCurrency.choices(),
        default=DatasetPriceCurrency.RUB.value
    )
