from django.utils.text import slugify

from external_services.datahub import DataHubDataset
from stock.consts import DatasetStatus
from stock.models import Dataset, DatasetPermissions, PricingDataset


class DatasetTurnkeyBuilder:

    def __init__(self, datahub_dataset: DataHubDataset):
        self._datahub_dataset = datahub_dataset
        self._dataset = None

    def _create_dataset(self):
        self._dataset, __ = Dataset.objects.get_or_create(
            external_id=self._datahub_dataset.urn,
            defaults={
                "name": self._datahub_dataset.name,
                "slug": slugify(self._datahub_dataset.name),
                "status": DatasetStatus.AVAILABLE.value,
                "is_active": True
            }
        )

    def _create_permissions(self):
        DatasetPermissions.objects.get_or_create(
            dataset=self._dataset,
            defaults={
                "is_public": True
            }
        )

    def _create_pricing(self):
        PricingDataset.objects.get_or_create(
            dataset=self._dataset,
            defaults={
                "is_free": True
            }
        )

    def build(self):
        self._create_dataset()
        self._create_permissions()
        self._create_pricing()
        return self._dataset
