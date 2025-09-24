from django.contrib import admin
from .models import Supplier, Supply, SupplyProduct



@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "inn", "company")
    search_fields = ("title", "inn")
    list_filter = ("company",)


class SupplyProductInline(admin.TabularInline):
    model = SupplyProduct
    extra = 1

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ("id", "supplier", "delivery_date")
    list_filter = ("supplier", "delivery_date")
    inlines = [SupplyProductInline]
