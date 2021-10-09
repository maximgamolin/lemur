from rest_framework import serializers

from plant.models import Workpiece, DataSampling
from stock.serializers import DatasetSerializer


class DataSamplingSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSampling
        fields = '__all__'


class WorkpieceSerializer(serializers.ModelSerializer):

    parental_datasets = DatasetSerializer(many=True)
    datasamples = DataSamplingSerializer(many=True)

    class Meta:
        model = Workpiece
        fields = ('id',
                  'name_of_dataset',
                  'parental_datasets',
                  'status',
                  'raw_joins',
                  'joins',
                  'raw_features',
                  'features',
                  'limits',
                  'datasamples')
