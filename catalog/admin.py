from django.contrib import admin

from catalog.models import (
    ProductCategory,
    Product,
)


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    list_display = [
        'name',
        'is_active',
        'slug'
    ]


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = [
        'title',
        'price',
        'category',
        'is_active',
        'slug',
        'admin_image'
    ]
    list_per_page = 20
    list_editable = [
        'price',
        'is_active'
    ]

