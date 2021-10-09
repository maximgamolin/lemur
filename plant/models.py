from django.db import models

from plant.consts import WorkpieceStatus, JoinType
from stock.consts import DatasetPriceCurrency


class Workpiece(models.Model):
    author = models.ForeignKey('core.User', on_delete=models.CASCADE)
    name_of_dataset = models.CharField(max_length=255)
    parental_datasets = models.ManyToManyField('stock.Dataset')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.PositiveSmallIntegerField(choices=WorkpieceStatus.choices(), default=WorkpieceStatus.CREATED.value)
    new_features = models.JSONField(null=True, blank=True)
    aggregation = models.JSONField(null=True, blank=True)
    limits = models.JSONField(null=True, blank=True)


class WorkpiecePricing(models.Model):
    workpiece = models.OneToOneField('plant.Workpiece', on_delete=models.CASCADE)
    is_free = models.BooleanField()
    price = models.DecimalField(max_digits=19, decimal_places=4)
    currency = models.PositiveSmallIntegerField(
        choices=DatasetPriceCurrency.choices(),
        default=DatasetPriceCurrency.RUB.value
    )


class DataSampling(models.Model):
    workpiece = models.ForeignKey('plant.Workpiece', on_delete=models.CASCADE, related_name='datasamples')
    dataset = models.ForeignKey('stock.Dataset', on_delete=models.CASCADE, related_name='datasamples')
    fields = models.JSONField(null=True, blank=True)
    filtering = models.JSONField(null=True, blank=True)
    aggregation = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DataSamplingUnionParent(models.Model):
    workpiece = models.ForeignKey('plant.Workpiece', on_delete=models.CASCADE)
    parental_data_sample = models.ForeignKey(
        'plant.DataSampling', on_delete=models.CASCADE, related_name='parental_sample'
    )
    child_data_sample = models.ForeignKey(
        'plant.DataSampling', on_delete=models.CASCADE, related_name='child_sample'
    )
    parental_column_name = models.CharField(max_length=255)
    child_column_name = models.CharField(max_length=255)
    join_type = models.PositiveSmallIntegerField(choices=JoinType.choices(), default=JoinType.INNER.value)

