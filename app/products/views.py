from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from .models import Product
from .serializers import ProductSerializer
from companies.permissions import IsCompanyOwnerOrEmployee



@extend_schema(tags=["Товары"])
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsCompanyOwnerOrEmployee]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(storage__company=user.company)


@extend_schema(tags=["Товары"])
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsCompanyOwnerOrEmployee]

    def get_queryset(self):
        return Product.objects.filter(storage__company=self.request.user.company)