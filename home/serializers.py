from rest_framework import serializers
from .models import Vendor, HistoricalPerformance,PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
    def to_representation(self, instance):
        # Convert the instance to a representation
        representation = super().to_representation(instance)

        # Include acknowledgment_date if available
        if instance.acknowledgment_date:
            representation['acknowledgment_date'] = instance.acknowledgment_date

        return representation
