from django.urls import path
from .views import IndexView, CategoryProductsBySlugView, CategoryProducts, ProductDetailsView, ContactView, SearchView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<slug:slug>/', CategoryProductsBySlugView.as_view(), name='category_products_by_slug'),
    path('category/', CategoryProducts.as_view(), name='category_products'),
    path('product/<slug:slug>/', ProductDetailsView.as_view(), name='product_details'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', SearchView.as_view(), name='search'),
]