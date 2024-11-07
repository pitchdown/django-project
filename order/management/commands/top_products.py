from django.core.management.base import BaseCommand
from django.db.models import Count
from store.models import Product
from order.models import CartItem

class Command(BaseCommand):
    help = 'Finds the top 3 most popular products in users carts'

    def handle(self, *args, **kwargs):
        top_products = (
            CartItem.objects.values('product')
            .annotate(num_users=Count('user', distinct=True))
            .order_by('-num_users')
        )

        top_3_products = top_products[:3]

        self.stdout.write("Top 3 most popular products:\n")
        for item in top_3_products:
            product = item['product']
            num_users = item['num_users']
            product_instance = Product.objects.get(id=product)
            self.stdout.write(f"Product: {product_instance.name}, Users: {num_users}")

