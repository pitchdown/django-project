from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from store.models import Product
from django.http import HttpResponse
from .models import CartItem



# Create your views here.
def order_cart(request):
    total_price_of_products = 0
    cart = request.session.get('cart', {})

    for product_id, product in cart.items():
        if 'every_product_total' not in product:
            product['every_product_total'] = 0
        product['total'] = float(product['price']) * product['quantity']
        total_price_of_products += float(product['total'])

    return render(request, 'cart.html', {
        'cart': cart,
        'total_price_of_products': total_price_of_products
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    print(product.quantity)

    if product.quantity != 0:
        if str(product.id) in cart:
            cart[str(product.id)]['quantity'] += 1
            print('wow')
        else:
            cart[str(product.id)] = {
                'name': product.name,
                'price': str(product.price),
                'quantity': 1,
                'image': str(product.image)
            }

        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user,
                                                                defaults={'quantity': 0})
        cart_item.quantity += 1
        cart_item.save()

        product.quantity -= 1
        product.save()
    else:
        messages.error(request, 'Product is out of stock. Please choose another product.')
        return redirect('category_products')

    request.session['cart'] = cart
    return redirect('order_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product = get_object_or_404(Product, id=product_id)

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart

    cart_item = CartItem.objects.get(product_id=product_id)

    product.quantity += cart_item.quantity
    product.save()
    cart_item.delete()

    return redirect('order_cart')

def checkout(request):
    total_price_of_products = 0
    cart = request.session.get('cart', {})

    for product_id, product in cart.items():
        if 'every_product_total' not in product:
            product['every_product_total'] = 0
        product['total'] = float(product['price']) * product['quantity']
        total_price_of_products += float(product['total'])

    return render(request, 'checkout.html', {
        'cart': cart,
        'total_price_of_products': total_price_of_products
    })