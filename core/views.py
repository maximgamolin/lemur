from django.views.generic import TemplateView
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import SchemaBlock


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


class SchemaBlockView(ListAPIView):

    class SchemaBlockSerializer(serializers.ModelSerializer):
        inPorts = serializers.JSONField(source='in_ports')
        outPorts = serializers.JSONField(source='out_ports')
        category = serializers.SerializerMethodField()
        type = serializers.SerializerMethodField()

        def get_category(self, obj):
            return obj.get_category_display()

        def get_type(self, obj):
            return obj.get_type_display()

        class Meta:
            model = SchemaBlock
            fields = ('inPorts', 'outPorts', 'category', 'type', 'id', 'name', 'title')

    def get_queryset(self):
        return SchemaBlock.objects.all()

    serializer_class = SchemaBlockSerializer



class PageView(TemplateView):
    template_name = 'index.html'

