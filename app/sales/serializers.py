from rest_framework import serializers
from .models import Sale, ProductSale
from products.models import Product


class ProductSaleSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = ProductSale
        fields = ["product", "quantity"]


class SaleSerializer(serializers.ModelSerializer):
    product_sales = ProductSaleSerializer(many=True, write_only=True)
    products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Sale
        fields = ["id", "buyer_name", "sale_date", "product_sales", "products"]

    def get_products(self, obj):
        return {
            ps.product.title: ps.quantity
            for ps in obj.product_sales.all()
        }

    def validate(self, data):
        company = self.context["request"].user.company
        errors = {}

        for item in data.get("product_sales", []):
            product = item["product"]
            quantity = item["quantity"]
            if product.storage.company != company:
                errors[product.title] = "Данного товара нет в наличии на вашем складе"
            elif product.quantity < quantity:
                errors[product.title] = f"В наличии только {product.quantity}"

        if errors:
            raise serializers.ValidationError(errors)
        return data

    def create(self, validated_data):
        product_sales_data = validated_data.pop("product_sales")
        request = self.context["request"]
        company = request.user.company

        sale = Sale.objects.create(
            company=company,
            created_by=request.user,
            **validated_data
        )

        for item in product_sales_data:
            product = item["product"]
            quantity = item["quantity"]

            ProductSale.objects.create(
                sale=sale,
                product=product,
                quantity=quantity
            )

            product.quantity -= quantity
            product.save()

        return sale

    def update(self, instance, validated_data):
        validated_data.pop("product_sales", None)
        return super().update(instance, validated_data)
