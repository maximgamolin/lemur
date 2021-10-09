from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from market.cases.add_to_collection import AddToCollectionService, AddToCollectionError
from market.models import CollectionItem, Collection
from stock.cases.dataset_access import DatasetUserAccess
from stock.serializers import DatasetSerializer


class CollectionItemView(APIView):
    permission_classes = [IsAuthenticated]

    class CreateCollectionItemSerializer(serializers.Serializer):
        dataset_id = serializers.IntegerField(min_value=1)

    class CollectionItemSerializer(serializers.ModelSerializer):

        dataset = DatasetSerializer()

        class Meta:
            model = CollectionItem
            fields = ('dataset', )

    def get(self, request, *args, **kwargs):
        collection, _ = Collection.objects.get_or_create(owner=self.request.user)
        collection_items = collection.collection_items.filter(is_active=True)
        response_serializer = self.CollectionItemSerializer(instance=collection_items, many=True)
        return Response(response_serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.CreateCollectionItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        avaliable_datasets = DatasetUserAccess(request.user).available_datasets

        service = AddToCollectionService(request.user, serializer.validated_data['dataset_id'], avaliable_datasets)
        try:
            collection_items = service.create_item()
        except AddToCollectionError as e:
            return Response({"detail": e}, status=400)
        response_serializer = self.CollectionItemSerializer(instance=collection_items, many=True)
        return Response(response_serializer.data)
