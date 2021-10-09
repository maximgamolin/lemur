from plant.models import DataSampling


class ConvertDatasetsToDataSamplesService:

    def __init__(self, workpiece, datasets):
        self._workpiece = workpiece
        self._datasets = datasets

    def convert(self):
        for dataset in self._datasets:
            DataSampling.objects.create(
                workpiece=self._workpiece,
                dataset=dataset,
                fields=dataset.fields
            )
        return self._workpiece