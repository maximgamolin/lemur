from django.db import transaction

from market.models import Collection
from plant.consts import WorkpieceStatus
from plant.models import Workpiece


class InitWorkpieceService:

    def __init__(self, user, name, collection):
        self._user = user
        self._name = name
        self._collection: Collection = collection
        self._workpiece = None

    def _configure_workpiece(self):
        self._workpiece = Workpiece.objects.create(
            author=self._user,
            name_of_dataset=self._name,
            status=WorkpieceStatus.CREATED.value
        )

    def _transfer_datasets_from_collection_to_workpiece(self):
        with transaction.atomic():
            datasets = self._collection.collection_items\
                .filter(is_active=True)\
                .select_related('dataset')\
                .select_for_update()\
                .values_list('dataset', flat=True)
            self._workpiece.parental_datasets.add(*datasets)
            self._collection.collection_items\
                .filter(is_active=True)\
                .update(is_active=False)

    def init_workpiece(self):
        self._configure_workpiece()
        self._transfer_datasets_from_collection_to_workpiece()
        return self._workpiece
