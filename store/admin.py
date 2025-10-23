from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "discount_price", "is_available", "created_at")
    list_filter = ("is_available", "category")
    search_fields = ("name", "category__name")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Basic Info", {"fields": ("name", "slug", "description", "category")}),
        ("Pricing", {"fields": ("price", "discount_price")}),
        ("Inventory", {"fields": ("stock", "is_available")}),
        ("Media", {"fields": ("thumbnail",)}),
        ("System", {"fields": ("created_by", "created_at", "updated_at")}),
    )