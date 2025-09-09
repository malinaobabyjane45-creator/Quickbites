from django import forms
from .models import Restaurant, MenuItem, Order

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address', 'phone', 'description']


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['restaurant', 'name', 'description', 'price', 'is_available']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['menu_item', 'customer_name', 'customer_address', 'quantity', 'total_price']
