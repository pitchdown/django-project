from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, TemplateView

# Create your views here.

class IndexView(ListView):
    """
    View for the index page that displays all products.
    """
    model = Product  # Specifies the model to use for this view
    template_name = 'index.html'  # Template to render
    context_object_name = 'products'  # Name of the context variable to access in the template


class CategoryProductsBySlugView(ListView):
    """
    View for displaying products in a specific category identified by a slug.
    """
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        """
        Returns a queryset of products filtered by the category slug passed in the URL.
        """
        return Product.objects.filter(categories__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        """
        Adds the category slug to the context for use in the template.
        """
        context = super().get_context_data(**kwargs)  # Get the default context
        context['slug'] = self.kwargs['slug']  # Add the slug to the context
        return context


class CategoryProducts(ListView):
    """
    View for displaying all products with pagination.
    """
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 3  # Number of products to display per page

    def get_queryset(self):
        """
        Returns all products for this view.
        """
        return Product.objects.all()


class ProductDetailsView(ListView):
    """
    View for displaying detailed information about a specific product.
    """
    model = Product
    template_name = 'shop-detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        """
        Returns a single product based on the slug passed in the URL.
        This method should actually return a queryset; consider using get_object_or_404 for clarity.
        """
        return Product.objects.get(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        """
        Adds related products and categories to the context for use in the detail template.
        """
        context = super().get_context_data(**kwargs)  # Get the default context
        context['products'] = Product.objects.all()  # Get all products to show on the detail page
        context['categories'] = context['product'].categories.all()  # Get categories related to the current product
        return context


class ContactView(TemplateView):
    """
    View for displaying the contact page.
    """
    template_name = 'contact.html'  # Template to render


class SearchView(ListView):
    """
    View for searching products by name.
    """
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        """
        Returns a queryset of products filtered by the search query provided in the URL.
        Uses case-insensitive containment.
        """
        return Product.objects.filter(name__icontains=self.request.GET.get('q'))
