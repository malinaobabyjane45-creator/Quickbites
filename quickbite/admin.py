from django.contrib import admin
from .models import Restaurant, MenuItem, Order

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'created_at')
    search_fields = ('name', 'address')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price', 'is_available')
    list_filter = ('is_available', 'restaurant')
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_item', 'customer_name', 'quantity', 'total_price', 'created_at')
    readonly_fields = ('total_price',)
