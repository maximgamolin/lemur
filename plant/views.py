from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from market.models import Collection
from plant.cases.conver_dataset_to_data_sample import ConvertDatasetsToDataSamplesService
from plant.cases.create_data_sample import CreateDataSampleService, \
    RawOperations
from plant.cases.init_workpiece import InitWorkpieceService
from plant.models import Workpiece, WorkpiecePricing
from plant.serializers import WorkpieceSerializer, WorkpiecePricingSerializer
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


class MoveDatasetToDataSampleView(APIView):

    class MoveDatasetToDataSampleSerializer(serializers.Serializer):
        datasets_ids = serializers.ListField(child=serializers.IntegerField(min_value=1))
        workpiece_id = serializers.IntegerField(min_value=1)

    def get(self, request, *args, **kwargs):
        qs = Workpiece.objects\
            .filter(author=self.request.user, is_active=True)
        serializer = WorkpieceSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_serializers = self.MoveDatasetToDataSampleSerializer(data=request.data)
        request_serializers.is_valid(raise_exception=True)
        datasets = Dataset.objects.filter(id__in=request_serializers.validated_data['datasets_ids'])
        workpiece = get_object_or_404(
            Workpiece,
            id=request_serializers.validated_data['workpiece_id'],
        )
        service = ConvertDatasetsToDataSamplesService(workpiece, datasets)
        workpiece = service.convert()
        response_serializer = WorkpieceSerializer(instance=workpiece)
        return Response(response_serializer.data)


class AddWorkpieceJoinsView(APIView):

    class AddWorkpieceJoinsSerializer(serializers.Serializer):
        workpiece_id = serializers.IntegerField(min_value=1)
        raw_joins = serializers.JSONField()

    def get(self, request, *args, **kwargs):
        qs = Workpiece.objects \
            .filter(author=self.request.user, is_active=True)
        serializer = WorkpieceSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_serializers = self.AddWorkpieceJoinsSerializer(data=request.data)
        request_serializers.is_valid(raise_exception=True)

        workpiece = get_object_or_404(
            Workpiece,
            id=request_serializers.validated_data['workpiece_id'],
        )
        workpiece.raw_joins = request_serializers.validated_data['raw_joins']
        workpiece.save()
        response_serializer = WorkpieceSerializer(instance=workpiece)
        return Response(response_serializer.data)


class AddWorkpieceFeatures(APIView):

    class AddWorkpieceFeaturesSerializer(serializers.Serializer):
        workpiece_id = serializers.IntegerField(min_value=1)
        raw_features = serializers.JSONField()

    def get(self, request, *args, **kwargs):
        qs = Workpiece.objects \
            .filter(author=self.request.user, is_active=True)
        serializer = WorkpieceSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_serializers = self.AddWorkpieceFeaturesSerializer(data=request.data)
        request_serializers.is_valid(raise_exception=True)

        workpiece = get_object_or_404(
            Workpiece,
            id=request_serializers.validated_data['workpiece_id'],
        )
        workpiece.raw_features = request_serializers.validated_data['raw_features']
        workpiece.save()
        response_serializer = WorkpieceSerializer(instance=workpiece)
        return Response(response_serializer.data)


class AddLimitsView(APIView):

    class AddWorkpieceLimitsSerializer(serializers.Serializer):
        workpiece_id = serializers.IntegerField(min_value=1)
        limits = serializers.JSONField()

    def get(self, request, *args, **kwargs):
        qs = Workpiece.objects \
            .filter(author=self.request.user, is_active=True)
        serializer = WorkpieceSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_serializers = self.AddWorkpieceLimitsSerializer(data=request.data)
        request_serializers.is_valid(raise_exception=True)

        workpiece = get_object_or_404(
            Workpiece,
            id=request_serializers.validated_data['workpiece_id'],
        )
        workpiece.limits = request_serializers.validated_data['limits']
        workpiece.save()
        response_serializer = WorkpieceSerializer(instance=workpiece)
        return Response(response_serializer.data)


class CreateTaskTextView(APIView):

    class CreateTaskTextSerializer(serializers.Serializer):
        workpiece_id = serializers.IntegerField(min_value=1)

    def get(self, request, *args, **kwargs):
        qs = Workpiece.objects \
            .filter(author=self.request.user, is_active=True)
        serializer = WorkpieceSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        request_serializers = self.CreateTaskTextSerializer(data=request.data)
        request_serializers.is_valid(raise_exception=True)

        workpiece = get_object_or_404(
            Workpiece,
            id=request_serializers.validated_data['workpiece_id'],
        )
        # TODO процессинг, докинуть прайсинг is_free, если никакого нет
        response_serializer = WorkpieceSerializer(instance=workpiece)
        return Response(response_serializer.data)


class SetWorkpiecePricingView(CreateAPIView):

    serializer_class = WorkpiecePricingSerializer

    def get_queryset(self):
        return WorkpiecePricing.objects.all()

    def get(self, request, *args, **kwargs):
        qs = Workpiece.objects \
            .filter(author=self.request.user, is_active=True)
        serializer = WorkpieceSerializer(instance=qs, many=True)
        return Response(serializer.data)


class CalculateResultDatasetPrelimPrice(serializers.Serializer):

    class CalculateResultDatasetPrelimSerializer(serializers.Serializer):
        workpiece_id = serializers.IntegerField(min_value=1)

    def get(self, request, *args, **kwargs):
        qs = Workpiece.objects \
            .filter(author=self.request.user, is_active=True)
        serializer = WorkpieceSerializer(instance=qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pass
