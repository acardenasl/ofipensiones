from django.urls import path
from .views import (PaymentReceiptList,
                    FacturaList
)

urlpatterns = [
    path("payment_receipt/", PaymentReceiptList.as_view(), name="payment_receipt_list"),
    path("factura/", FacturaList.as_view(), name="factura_list"),
]
