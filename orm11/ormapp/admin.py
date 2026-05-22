from django.contrib import admin
from .models import FoodOrder

class FoodOrderAdmin(admin.ModelAdmin):
    list_display = (
        'Order_ID',
        'CustomerName',
        'RestaurantName',
        'FoodItem',
        'Quantity',
        'Price',
        'DeliveryAddress',
        'OrderStatus'
    )

admin.site.register(FoodOrder, FoodOrderAdmin)