# urls.py

from django.urls import path
from .views import VendorListView, VendorDetailView, PurchaseOrderListView

urlpatterns = [
    path('vendors/', VendorListView.as_view(), name='vendor-list'),
    path('vendors/<int:vendor_id>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('purchase-orders/', PurchaseOrderListView.as_view(), name='purchase-order-list'),
]
