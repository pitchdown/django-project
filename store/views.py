from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def category_products_by_id(request, category_id):
    products = Product.objects.filter(categories__id=category_id)
    categories = Category.objects.all()
    return render(request, 'shop.html', {
        'products': products,
        'categories': categories
    })

def category_products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop.html', {
        'products': products,
        'categories': categories
    })


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    products = Product.objects.all()
    categories = product.categories.all()
    return render(request, 'shop-detail.html', {
        'product': product,
        'products': products,
        'categories': categories
    })


def contact(request):
    return render(request, 'contact.html')