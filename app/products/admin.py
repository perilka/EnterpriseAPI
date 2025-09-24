from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "storage", "quantity", "purchase_price", "sale_price")
    list_filter = ("storage__company",)
    search_fields = ("title",)
