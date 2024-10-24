from django.db.models import Sum
from store.models import Category
from order.models import CartItem


def cart_and_categories(request):
    categories = Category.objects.all()
    cart_item_count = 0

    if request.user.is_authenticated:
        cart_item_count = CartItem.objects.filter(user=request.user).aggregate(total_quantity=Sum('quantity'))[
                              'total_quantity'] or 0

    return {
        'categories': categories,
        'cart_item_count': cart_item_count,
    }