from django.db import models
from products.models import Product



class Supplier(models.Model):
    company = models.ForeignKey("companies.Company", on_delete=models.CASCADE, related_name="suppliers")
    title = models.CharField(max_length=255)
    inn = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.title} ({self.inn})"


class Supply(models.Model):
    supplier = models.ForeignKey("suppliers.Supplier", on_delete=models.CASCADE, related_name="supplies")
    delivery_date = models.DateTimeField()

    def __str__(self):
        return f"Поставка №{self.id} от {self.supplier.title}"


class SupplyProduct(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE, related_name="supply_products")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.title} x {self.quantity} (поставка {self.supply.id})"