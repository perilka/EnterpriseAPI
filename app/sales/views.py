from django.db import transaction
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Sale
from .serializers import SaleSerializer
from companies.permissions import IsCompanyOwnerOrEmployee


@extend_schema(tags=["Продажи"])
class SaleListCreateView(generics.ListCreateAPIView):
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated, IsCompanyOwnerOrEmployee]

    def get_queryset(self):
        queryset = Sale.objects.filter(company=self.request.user.company)

        date_from = self.request.query_params.get("date_from")
        date_to = self.request.query_params.get("date_to")

        if date_from:
            queryset = queryset.filter(sale_date__gte=date_from)
        if date_to:
            queryset = queryset.filter(sale_date__lte=date_to)

        return queryset

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save()


@extend_schema(tags=["Продажи"])
class SaleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated, IsCompanyOwnerOrEmployee]

    def get_queryset(self):
        return Sale.objects.filter(company=self.request.user.company)

    @transaction.atomic
    def perform_destroy(self, instance):
        for ps in instance.product_sales.all():
            ps.product.quantity += ps.quantity
            ps.product.save()
        instance.delete()
