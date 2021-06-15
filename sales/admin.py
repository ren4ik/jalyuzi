from django.contrib import admin

from sales.models import Order


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = [
        'client_name',
        'order_id',
        'contact',
        'product',
        'price',
        'pub_date',
        'is_delivered',
        'delivered_date'
    ]
    list_editable = [
        'contact',
        'product',
    ]
    list_per_page = 20
    list_filter = [
        'is_delivered',
    ]
