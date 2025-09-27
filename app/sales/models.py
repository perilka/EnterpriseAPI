from django.db import models
from companies.models import Company
from products.models import Product
from authenticate.models import User


class Sale(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="sales")
    buyer_name = models.CharField(max_length=255)
    sale_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="sales")

    def __str__(self):
        return f"Продажа №{self.id} (для {self.buyer_name})"


class ProductSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="product_sales")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_sales")
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.title} x {self.quantity} (Продажа №{self.sale.id})"

