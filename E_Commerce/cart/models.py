from django.db import models
from django.contrib.auth.models import User
from products.models import *

# Create your models here.
class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_cart") 
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_item")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"