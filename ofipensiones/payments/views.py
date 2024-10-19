from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OfipensionesLog, TermPayment
from .serializers import PaymentReceiptSerializer, FacturaSerializer
from .models import TermPayment, Factura
from django.http import Http404



import time
from datetime import timedelta



class PaymentReceiptList(APIView):
    def get(self, request):
        s = time.time()
        payment_receipts = TermPayment.objects.all()
        serializer = PaymentReceiptSerializer(payment_receipts, many=True)
        e = time.time()

        delta = timedelta(seconds=e - s)

        OfipensionesLog(operation_name="payment_receipts", time_taken=delta).save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    


class FacturaList(APIView):
    def get(self, request):
        s = time.time()
        factura = Factura.objects.all()
        serializer = FacturaSerializer(factura, many=True)
        e = time.time()
        
        delta = timedelta(seconds=e - s)
        OfipensionesLog(operation_name="facturas", time_taken=delta).save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        s = time.time()
        serializer = FacturaSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            e = time.time()
            
            delta = timedelta(seconds=e - s)
            OfipensionesLog(operation_name="create_factura", time_taken=delta).save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        e = time.time()
        delta = timedelta(seconds=e - s)
        OfipensionesLog(operation_name="create_factura_failed", time_taken=delta).save()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class FacturaDetail(APIView):
    """
    Retrieve, update, or delete a Factura instance.
    """
    def get_object(self, pk):
        try:
            return Factura.objects.get(pk=pk)
        except Factura.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        s = time.time()
        factura = self.get_object(pk)
        serializer = FacturaSerializer(factura)
        e = time.time()

        delta = timedelta(seconds=e - s)
        OfipensionesLog(operation_name="retrieve_factura", time_taken=delta).save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        s = time.time()
        factura = self.get_object(pk)
        serializer = FacturaSerializer(factura, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            e = time.time()

            delta = timedelta(seconds=e - s)
            OfipensionesLog(operation_name="update_factura", time_taken=delta).save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        e = time.time()
        delta = timedelta(seconds=e - s)
        OfipensionesLog(operation_name="update_factura_failed", time_taken=delta).save()

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        s = time.time()
        factura = self.get_object(pk)
        factura.delete()
        e = time.time()

        delta = timedelta(seconds=e - s)
        OfipensionesLog(operation_name="delete_factura", time_taken=delta).save()

        return Response(status=status.HTTP_204_NO_CONTENT)
