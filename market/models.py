from django.db import models


class Collection(models.Model):
    owner = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='collections')


class CollectionItem(models.Model):
    dataset = models.ForeignKey('stock.Dataset', on_delete=models.CASCADE, related_name='collection_item')
