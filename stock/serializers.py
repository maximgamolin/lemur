from rest_framework import serializers

from stock.models import Dataset, PricingDataset


class PricingDatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingDataset
        fields = '__all__'


class DatasetSerializer(serializers.ModelSerializer):

    pricing = PricingDatasetSerializer()

    class Meta:
        model = Dataset
        fields = '__all__'
