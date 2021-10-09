from rest_framework.generics import ListAPIView
from stock.cases import dataset_access
from rest_framework import serializers
from stock.models import Dataset


class DatasetListView(ListAPIView):

    class DatasetSerializer(serializers.ModelSerializer):

        class Meta:
            model = Dataset
            fields = '__all__'

    serializer_class = DatasetSerializer

    def get_queryset(self):
        return dataset_access.DatasetUserAccess(self.request.user).available_datasets
