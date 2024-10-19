from django.urls import path
from .views import BillDetail, PaymentReceiptList, BillList


urlpatterns = [
    path("payment_receipts/", PaymentReceiptList.as_view()),
    path("bills/", BillList.as_view()),
    path("bills/<int:pk>", BillDetail.as_view()),
]
