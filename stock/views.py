from rest_framework.generics import ListAPIView

from stock.cases import dataset_access
from stock.serializers import DatasetSerializer


class DatasetListView(ListAPIView):

    serializer_class = DatasetSerializer

    def get_queryset(self):
        return dataset_access.DatasetUserAccess(self.request.user).available_datasets
