from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.response import Response


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    class UserWithBillSerializer(serializers.Serializer):

        id = serializers.IntegerField()
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        bill_amount = serializers.DecimalField(max_digits=19, decimal_places=4, source='bill.amount')
        currency = serializers.DecimalField(max_digits=19, decimal_places=4, source='bill.currency')

    serializer_class = UserWithBillSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=request.user)
        return Response(serializer.data)

