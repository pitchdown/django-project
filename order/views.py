from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from store.models import Product
from django.http import HttpResponse
from .models import CartItem
from django.views.generic import ListView, View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class OrderCartView(LoginRequiredMixin, TemplateView):
    """
    View for displaying the shopping cart.
    """
    template_name = 'cart.html'  # Template to render for the cart view

    def get_context_data(self, **kwargs):
        """
        Adds the cart and total price information to the context.
        """
        context = super().get_context_data(**kwargs)  # Get the default context
        total_price_of_products = 0  # Initialize total price counter
        cart = self.request.session.get('cart', {})  # Retrieve the cart from the session

        # Calculate total prices for each product in the cart
        for product_id, product in cart.items():
            if 'every_product_total' not in product:
                product['every_product_total'] = 0  # Initialize if not present
            product['total'] = float(product['price']) * product['quantity']  # Calculate total for this product
            total_price_of_products += float(product['total'])  # Update total price

        context['cart'] = cart  # Add cart to context
        context['total_price_of_products'] = total_price_of_products  # Add total price to context
        return context

    def dispatch(self, request, *args, **kwargs):
        """
        Check if the user is authenticated before processing the request.
        Redirect to sign-up if not authenticated.
        """
        if not request.user.is_authenticated:
            messages.error(request, 'You need to sign up or sign in to view your cart.')
            return redirect('sign_up')  # Redirect to the sign-up page
        return super().dispatch(request, *args, **kwargs)


class AddToCartView(View):
    """
    View for adding a product to the shopping cart.
    """
    def post(self, request, product_id):
        """
        Handles POST requests to add a product to the cart.
        """
        if not request.user.is_authenticated:
            messages.error(request, 'you need to sign up or sign in to add products to the cart')
            return redirect('sign_up')

        product = get_object_or_404(Product, id=product_id)  # Get the product or return a 404 if not found
        cart = request.session.get('cart', {})  # Retrieve the cart from the session

        if product.quantity != 0:  # Check if the product is in stock
            if str(product.id) in cart:  # If the product is already in the cart
                cart[str(product.id)]['quantity'] += 1  # Increase quantity
            else:
                # Add new product to the cart
                cart[str(product.id)] = {
                    'name': product.name,
                    'price': str(product.price),
                    'quantity': 1,
                    'image': str(product.image)
                }

            # Update the CartItem model for persistent storage
            cart_item, created = CartItem.objects.get_or_create(
                product=product,
                user=request.user,
                defaults={'quantity': 0}  # Default quantity if creating a new CartItem
            )
            cart_item.quantity += 1  # Increment quantity in CartItem
            cart_item.save()  # Save changes

            product.quantity -= 1  # Decrease product stock
            product.save()  # Save product changes
        else:
            messages.error(request, 'Product is out of stock. Please choose another product.')  # Show error message
            return redirect('category_products')  # Redirect to the category page if out of stock

        request.session['cart'] = cart  # Save updated cart back to the session
        return redirect('order_cart')  # Redirect to the cart view


class RemoveFromCartView(View):
    """
    View for removing a product from the shopping cart.
    """
    def post(self, request, product_id):
        """
        Handles POST requests to remove a product from the cart.
        """
        if not request.user.is_authenticated:
            messages.error(request, 'you need to sign up or sign in to remove products from the cart')
            return redirect('sign_up')

        cart = request.session.get('cart', {})  # Retrieve the cart from the session
        product = get_object_or_404(Product, id=product_id)  # Get the product or return a 404 if not found

        # Check if the product is in the cart
        if str(product_id) in cart:
            if cart[str(product_id)]['quantity'] > 1:
                # Decrease the quantity by 1
                cart[str(product_id)]['quantity'] -= 1

                # Update the CartItem in the database
                cart_item = get_object_or_404(CartItem, product=product, user=request.user)
                cart_item.quantity -= 1
                cart_item.save()

                messages.success(request, f"Reduced quantity of {product.name} in your cart.")
            else:
                # Remove product completely from the cart
                del cart[str(product_id)]

                # Remove CartItem from the database
                cart_item = get_object_or_404(CartItem, product=product, user=request.user)
                cart_item.delete()

                messages.success(request, f"{product.name} has been removed from your cart.")

            # Update the product stock
            product.quantity += 1  # Restore product stock
            product.save()  # Save product changes
        else:
            messages.error(request, "This item is not in your cart.")

        request.session['cart'] = cart  # Save updated cart back to the session
        return redirect('order_cart')  # Redirect to the cart view



class CheckoutView(LoginRequiredMixin, TemplateView):
    """
    View for displaying the checkout page.
    """
    template_name = 'checkout.html'  # Template to render for the checkout view

    def get_context_data(self, **kwargs):
        """
        Adds the cart and total price information to the context for checkout.
        """
        context = super().get_context_data(**kwargs)  # Get the default context
        total_price_of_products = 0  # Initialize total price counter
        cart = self.request.session.get('cart', {})  # Retrieve the cart from the session

        # Calculate total prices for each product in the cart
        for product_id, product in cart.items():
            if 'every_product_total' not in product:
                product['every_product_total'] = 0  # Initialize if not present
            product['total'] = float(product['price']) * product['quantity']  # Calculate total for this product
            total_price_of_products += float(product['total'])  # Update total price

        context['cart'] = cart  # Add cart to context
        context['total_price_of_products'] = total_price_of_products  # Add total price to context
        return context

    def dispatch(self, request, *args, **kwargs):
        """
        Check if the user is authenticated before processing the request.
        Redirect to sign-up if not authenticated.
        """
        if not request.user.is_authenticated:
            messages.error(request, 'You need to sign up or sign in to access the checkout.')
            return redirect('sign_up')  # Redirect to the sign-up page
        return super().dispatch(request, *args, **kwargs)