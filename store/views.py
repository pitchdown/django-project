from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def category_products_by_slug(request, slug):
    products = Product.objects.filter(categories__slug=slug)
    return render(request, 'shop.html', {
        'products': products,
        'slug': slug
    })

def category_products(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 3)

    page_number = request.GET.get('page')
    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, 'shop.html', {
        'products': products,
    })


def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    products = Product.objects.all()
    categories = product.categories.all()
    return render(request, 'shop-detail.html', {
        'product': product,
        'products': products,
        'categories': categories
    })


def contact(request):
    return render(request, 'contact.html')


def search(request):
    q = request.GET.get('q', None)

    if q:
        products = Product.objects.filter(name__icontains=q)
    else:
        products = Product.objects.all()

    return render(request, 'shop.html', {'products': products})