from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.contrib.auth import get_user_model

# Create your models here.
class CartItem(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.user}, {self.product}, {self.quantity}'