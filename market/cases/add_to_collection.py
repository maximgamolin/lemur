from market.models import CollectionItem, Collection


class AddToCollectionError(Exception):

    def __init__(self, msg):
        self._msg = msg


class AddToCollectionService:

    def __init__(self, user, dataset_id, available_datasets):
        self._user = user
        self._dataset_id = dataset_id
        self._available_datasets = available_datasets
        self._collection = None
        self._dataset = None
        self._collection_item = None

    def _get_or_create_collection(self):
        self._collection, _ = Collection.objects.get_or_create(owner=self._user)

    def _find_dataset(self):
        dataset = self._available_datasets.filter(id=self._dataset_id).first()
        if not dataset:
            raise AddToCollectionError("Датасет ненайден")
        self._dataset = dataset

    def _create_collection_item(self):
        self._collection_item = CollectionItem.objects.create(
            collection=self._collection,
            dataset=self._dataset
        )

    def create_item(self):
        self._get_or_create_collection()
        self._find_dataset()
        self._create_collection_item()
        return self._collection.collection_items.filter(is_active=True)