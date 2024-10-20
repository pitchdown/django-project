from django.urls import path
from .views import index, category_products_by_id, product_details, contact, category_products


urlpatterns = [
    path('', index, name='index'),
    path('products/category/<int:category_id>/', category_products_by_id, name='category_products_by_id'),
    path('products/category/', category_products, name='category_products'),
    path('product/<int:product_id>/', product_details, name='product_details'),
    path('contact/', contact, name='contact'),
]
