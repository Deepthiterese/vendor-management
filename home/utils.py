from django.db.models import Count, Avg,F
from .models import PurchaseOrder

def calculate_performance_metrics(vendor_id):
    # Calculate On-Time Delivery Rate
    completed_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id, status='completed')
    total_completed_pos = completed_pos.count()
    on_time_delivered_pos = completed_pos.filter(delivery_date__lte=F('delivery_date')).count()
    on_time_delivery_rate = on_time_delivered_pos / total_completed_pos if total_completed_pos > 0 else 0

    # Calculate Quality Rating Average
    quality_rating_avg = PurchaseOrder.objects.filter(vendor_id=vendor_id, quality_rating__isnull=False).aggregate(avg_rating=Avg('quality_rating'))['avg_rating'] or 0

    # Calculate Average Response Time
    average_response_time = PurchaseOrder.objects.filter(vendor_id=vendor_id, acknowledgment_date__isnull=False).aggregate(avg_response=Avg(F('acknowledgment_date') - F('issue_date')))['avg_response'] or 0

    # Calculate Fulfilment Rate
    total_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id).count()
    fulfilled_pos = PurchaseOrder.objects.filter(vendor_id=vendor_id, status='completed').count()
    fulfillment_rate = fulfilled_pos / total_pos if total_pos > 0 else 0

    return {
        'on_time_delivery_rate': on_time_delivery_rate,
        'quality_rating_avg': quality_rating_avg,
        'average_response_time': average_response_time.total_seconds() if average_response_time else 0,
        'fulfillment_rate': fulfillment_rate
    }
