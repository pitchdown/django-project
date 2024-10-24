from django.urls import path
from .views import index, category_products_by_slug, product_details, contact, category_products, search


urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:slug>/', category_products_by_slug, name='category_products_by_slug'),
    path('category/', category_products, name='category_products'),
    path('product/<slug:slug>/', product_details, name='product_details'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
]
