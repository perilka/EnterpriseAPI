from django.urls import path
from .views import SupplierListCreateView, SupplierDetailView, SupplyListCreateView

urlpatterns = [
    path("suppliers/", SupplierListCreateView.as_view(), name="supplier-list-create"),
    path("suppliers/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
    path("supplies/", SupplyListCreateView.as_view(), name="supply-list-create"),
]