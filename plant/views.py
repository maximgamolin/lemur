from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from market.models import Collection
from plant.cases.create_data_sample import CreateDataSampleService, \
    RawOperations
from plant.cases.init_workpiece import InitWorkpieceService
from plant.models import Workpiece
from plant.serializers import WorkpieceSerializer
from stock.models import Dataset


class InitWorkpieceView(APIView):

    permission_classes = [IsAuthenticated]

    class InitWorkpieceSerializer(serializers.Serializer):
        name = serializers.CharField()

    def get(self, request, *args, **kwargs):
        qs = Workpiece.objects\
            .filter(author=self.request.user, is_active=True)
        serializer = WorkpieceSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_serializer = self.InitWorkpieceSerializer(
            data=request.data
        )
        request_serializer.is_valid(raise_exception=True)
        collection = get_object_or_404(
            Collection, owner=self.request.user
        )
        service = InitWorkpieceService(
            request.user,
            request_serializer.validated_data['name'],
            collection
        )
        workpiece = service.init_workpiece()
        response_serializer = WorkpieceSerializer(
            instance=workpiece
        )
        return Response(response_serializer.data)


class WorkpieceDetailView(RetrieveAPIView):

    serializer_class = WorkpieceSerializer

    def get_queryset(self):
        return Workpiece.objects\
            .filter(author=self.request.user, is_active=True)


class CreateDataSampleView(APIView):

    permission_classes = [IsAuthenticated]

    class CreateDataSampleSerializer(serializers.Serializer):
        dataset_id = serializers.IntegerField(min_value=1)
        workpiece_id = serializers.IntegerField(min_value=1)
        raw_filtering = serializers.JSONField()
        raw_aggregation = serializers.JSONField()
        raw_features = serializers.JSONField()

    def get(self, request, *args, **kwargs):
        qs = Workpiece.objects\
            .filter(author=self.request.user, is_active=True)
        serializer = WorkpieceSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.CreateDataSampleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        raw_operations = RawOperations(
            filtering=serializer.validated_data['raw_filtering'],
            aggregation=serializer.validated_data['raw_aggregation'],
            features=serializer.validated_data['raw_features']
        )
        workpiece = get_object_or_404(
            Workpiece,
            id=serializer.validated_data['workpiece_id'],
        )
        dataset = get_object_or_404(
            Dataset,
            id=serializer.validated_data['dataset_id']
        )  # Косяк - тут нужна проверка доступности конкретного датасета для пользователя
        service = CreateDataSampleService(
            workpiece,
            dataset,
            raw_operations
        )
        workpiece = service.create_data_sample()
        response_serializer = WorkpieceSerializer(instance=workpiece)
        return Response(response_serializer.data)