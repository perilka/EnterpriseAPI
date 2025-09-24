from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .models import Supplier, Supply
from .serializers import SupplierSerializer, SupplySerializer
from companies.permissions import IsCompanyOwnerOrEmployee


@extend_schema(tags=["Поставщики"])
class SupplierListCreateView(generics.ListCreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsCompanyOwnerOrEmployee]

    def get_queryset(self):
        user = self.request.user
        return Supplier.objects.filter(company=user.company)


@extend_schema(tags=["Поставщики"])
class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsCompanyOwnerOrEmployee]

    def get_queryset(self):
        return Supplier.objects.filter(company=self.request.user.company)


@extend_schema(tags=["Поставки"])
class SupplyListCreateView(generics.ListCreateAPIView):
    serializer_class = SupplySerializer
    permission_classes = [IsAuthenticated, IsCompanyOwnerOrEmployee]

    def get_queryset(self):
        return Supply.objects.filter(supplier__company=self.request.user.company)

    def perform_create(self, serializer):
        serializer.save()