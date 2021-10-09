from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from external_services.datahub import DataHubConnector, DataHubError
from stock.cases import dataset_access
from stock.cases.builder import DatasetTurnkeyBuilder
from stock.models import Dataset
from stock.serializers import DatasetSerializer


class DatasetListView(ListAPIView):

    serializer_class = DatasetSerializer

    def get_queryset(self):
        return dataset_access.DatasetUserAccess(self.request.user).available_datasets


class DatasetSearchView(APIView):

    def update_db(self, datahub_datasets):
        result = []
        for i in datahub_datasets:
            result.append(DatasetTurnkeyBuilder(i).build())
        return result

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if not query:
            return Response(DatasetSerializer(instance=Dataset.objects.none(), many=True).data)
        connector = DataHubConnector()
        try:
            results = connector.search(query)
        except DataHubError as e:
            return Response({"detail": e}, status=400)
        datasets = self.update_db(results)
        qs = Dataset.objects.filter(id__in=[i.id for i in datasets])
        serializer = DatasetSerializer(instance=qs, many=True)
        return Response(serializer.data)

