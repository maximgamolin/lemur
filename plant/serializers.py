from rest_framework import serializers

from plant.models import Workpiece
from stock.serializers import DatasetSerializer


class WorkpieceSerializer(serializers.ModelSerializer):

    parental_datasets = DatasetSerializer(many=True)

    class Meta:
        model = Workpiece
        fields = ('name_of_dataset',
                  'parental_datasets',
                  'status',
                  'new_features',
                  'aggregation')
