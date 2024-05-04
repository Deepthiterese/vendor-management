from rest_framework.views import APIView  
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer
from datetime import datetime
from .utils import calculate_performance_metrics



class MyAuthenticatedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
       
        return Response("Authenticated View")


class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

#class VendorPerformanceAPIView(generics.RetrieveAPIView):
    #queryset = Vendor.objects.all()
    #serializer_class = VendorPerformanceSerializer
    #lookup_url_kwarg = 'vendor_id'

    #def retrieve(self, request, *args, **kwargs):
        #vendor = self.get_object()
        #serializer = self.get_serializer(vendor)
        #return Response(serializer.data)

##class PurchaseOrderAcknowledgeAPIView(generics.UpdateAPIView):
    ##serializer_class = PurchaseOrderSerializer
   # lookup_url_kwarg = 'po_id'
    #http_method_names = ['post']

    #def perform_update(self, serializer):
       # instance = serializer.save()
        #if instance.acknowledgment_date:
           # instance.calculate_response_time()
class VendorPerformanceAPIView(generics.RetrieveAPIView):
    serializer_class = VendorPerformanceSerializer
    lookup_url_kwarg = 'vendor_id'  # Update this line to use "vendor_code"

    def get_queryset(self):
        vendor_id = self.kwargs.get(self.lookup_url_kwarg)
        return Vendor.objects.filter(id=vendor_id)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        performance_metrics = calculate_performance_metrics(instance.id)
        serializer = self.get_serializer(performance_metrics)
        return Response(serializer.data)
           


#class PurchaseOrderAcknowledgeAPIView(generics.CreateAPIView):
   # queryset = PurchaseOrder.objects.all()
   # serializer_class = PurchaseOrderSerializer
    #lookup_url_kwarg = 'po_id'
    #http_method_names = ['post']

   # def create(self, request, *args, **kwargs):
        # Custom logic for acknowledging a purchase order
        
        #serializer = self.get_serializer(data=request.data)
       # if serializer.is_valid():
            #serializer.save()
            # Perform additional actions after successful creation
           # return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #def perform_update(self, serializer):
        #instance = serializer.save(acknowledgment_date=datetime.now())  # Update acknowledgment_date
        #instance.calculate_response_time()  # Recalculate response time if needed


class PurchaseOrderAcknowledgeAPIView(APIView):
    def post(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=po_id)
        except PurchaseOrder.DoesNotExist:
            return Response({"detail": "Purchase order does not exist."}, status=status.HTTP_404_NOT_FOUND)

        purchase_order.acknowledgment_date = datetime.now()
        purchase_order.save()
        purchase_order.calculate_response_time()

        return Response({"message": "Purchase order acknowledged successfully."}, status=status.HTTP_200_OK)
