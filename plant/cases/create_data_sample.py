from collections import namedtuple

from plant.models import DataSampling
from stock.models import Dataset

RawOperations = namedtuple('RawOperations', ['filtering', 'aggregation', 'features'])


class CreateDataSampleService:

    def __init__(self, workpiece,
                 dataset: Dataset,
                 name,
                 raw_operations: RawOperations):
        self._name = name
        self._workpiece = workpiece
        self._dataset = dataset
        self._raw_operations = raw_operations
        self._data_sample = None

    def _configure_data_sample(self):
        self._data_sample = DataSampling.objects.create(
            workpiece=self._workpiece,
            dataset=self._dataset,
            raw_filtering=self._raw_operations.filtering,
            raw_aggregation=self._raw_operations.aggregation,
            raw_features=self._raw_operations.features,
            fields=self._dataset.fields,
            name=self._name
        )

    def _raw_filters_to_filters(self):
        pass

    def _raw_aggregations_to_aggregations(self):
        pass

    def _raw_features_to_features(self):
        pass

    def create_data_sample(self):
        self._configure_data_sample()
        self._raw_features_to_features()
        self._raw_aggregations_to_aggregations()
        self._raw_features_to_features()
        return self._workpiece
