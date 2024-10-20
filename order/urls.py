from django.urls import path
from .views import order_cart, checkout, add_to_cart, remove_from_cart


urlpatterns = [
    path('order/cart/', order_cart, name='order_cart'),
    path('order/checkout/', checkout, name='order_checkout'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart')
]