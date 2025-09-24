from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "purchase_price", "sale_price", "quantity", "storage"]
        read_only_fields = ["quantity"]

        def validate_storage(self, value):
            user = self.context['request'].user
            if value.company != user.company:
                raise serializers.ValidationError("Нельзя создать товар в чужой компании")
            return value