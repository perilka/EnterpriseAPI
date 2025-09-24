from rest_framework import serializers
from .models import Supplier, Supply, SupplyProduct



class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["id", "title", "inn", "company"]
        read_only_fields = ["company"]


class SupplyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyProduct
        fields = ["product", "quantity"]


class SupplySerializer(serializers.ModelSerializer):
    products = SupplyProductSerializer(many=True, write_only=True)
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())

    class Meta:
        model = Supply
        fields = ["id", "supplier", "delivery_date", "products"]

    def create(self, validated_data):
        products_data = validated_data.pop("products")
        supply = Supply.objects.create(**validated_data)

        for item in products_data:
            product = item["product"]
            quantity = item["quantity"]
            if quantity <= 0:
                raise serializers.ValidationError("Количество товара должно быть положительным числом.")
            SupplyProduct.objects.create(supply=supply, product=product, quantity=quantity)
            product.quantity += quantity
            product.save()

        return supply