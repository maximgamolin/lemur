from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from market.models import Collection
from plant.cases.init_workpiece import InitWorkpieceService
from plant.models import Workpiece
from plant.serializers import WorkpieceSerializer


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


