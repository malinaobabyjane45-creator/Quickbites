from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurants/new/', views.RestaurantCreateView.as_view(), name='restaurant_create'),
    path('restaurants/<int:pk>/edit/', views.RestaurantUpdateView.as_view(), name='restaurant_update'),
    path('restaurants/<int:pk>/delete/', views.RestaurantDeleteView.as_view(), name='restaurant_delete'),
    path('restaurants/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant_detail'),

    path('menu/', views.MenuItemListView.as_view(), name='menuitem_list'),
    path('menu/new/', views.MenuItemCreateView.as_view(), name='menuitem_create'),
    path('menu/<int:pk>/edit/', views.MenuItemUpdateView.as_view(), name='menuitem_update'),
    path('menu/<int:pk>/delete/', views.MenuItemDeleteView.as_view(), name='menuitem_delete'),
    path('menu/<int:pk>/', views.MenuItemDetailView.as_view(), name='menuitem_detail'),

    path('order/new/', views.create_order, name='create_order'),
    path('order/success/<int:pk>/', views.order_success, name='order_success'),

    path('search/', views.search, name='search'),
]
