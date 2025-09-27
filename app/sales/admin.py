from django.contrib import admin
from .models import Sale, ProductSale


class ProductSaleInline(admin.TabularInline):
    model = ProductSale
    extra = 0


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("id", "buyer_name", "company", "sale_date", "created_by")
    list_filter = ("company", "sale_date")
    search_fields = ("buyer_name",)
    inlines = [ProductSaleInline]

