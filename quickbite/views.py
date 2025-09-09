from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Restaurant, MenuItem, Order
from .forms import RestaurantForm, MenuItemForm, OrderForm
from decimal import Decimal

# Restaurants
class RestaurantListView(generic.ListView):
    model = Restaurant
    template_name = 'delivery/restaurant_list.html'
    context_object_name = 'restaurants'
    paginate_by = 10

class RestaurantCreateView(generic.CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'delivery/restaurant_form.html'

class RestaurantUpdateView(generic.UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'delivery/restaurant_form.html'

class RestaurantDetailView(generic.DetailView):
    model = Restaurant
    template_name = 'delivery/restaurant_detail.html'
    context_object_name = 'restaurant'

class RestaurantDeleteView(generic.DeleteView):
    model = Restaurant
    success_url = reverse_lazy('restaurant_list')
    template_name = 'delivery/confirm_delete.html'

# Menu Items
class MenuItemListView(generic.ListView):
    model = MenuItem
    template_name = 'delivery/menuitem_list.html'
    context_object_name = 'menuitems'
    paginate_by = 12

class MenuItemCreateView(generic.CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'delivery/menuitem_form.html'

class MenuItemUpdateView(generic.UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'delivery/menuitem_form.html'

class MenuItemDetailView(generic.DetailView):
    model = MenuItem
    template_name = 'delivery/menuitem_detail.html'
    context_object_name = 'menuitem'

class MenuItemDeleteView(generic.DeleteView):
    model = MenuItem
    success_url = reverse_lazy('menuitem_list')
    template_name = 'delivery/confirm_delete.html'

# Orders
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = Decimal(order.menu_item.price) * order.quantity
            order.save()
            return redirect('order_success', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'delivery/order_form.html', {'form': form})

def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'delivery/order_success.html', {'order': order})

# Search
def search(request):
    q = request.GET.get('q', '').strip()
    restaurants = MenuItems = []  # defaults
    results = []
    if q:
        restaurants = Restaurant.objects.filter(
            Q(name__icontains=q) | Q(address__icontains=q) | Q(description__icontains=q)
        )
        menu_items = MenuItem.objects.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
        ).select_related('restaurant')
        results = {
            'restaurants': restaurants,
            'menu_items': menu_items,
            'query': q
        }
    else:
        results = {
            'restaurants': Restaurant.objects.none(),
            'menu_items': MenuItem.objects.none(),
            'query': q
        }
    return render(request, 'delivery/search_results.html', results)
