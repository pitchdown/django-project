from django.urls import path
from .views import OrderCartView, CheckoutView, AddToCartView, RemoveFromCartView


urlpatterns = [
    path('order/cart/', OrderCartView.as_view(), name='order_cart'),
    path('order/checkout/', CheckoutView.as_view(), name='order_checkout'),
    path('add-to-cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart')
]