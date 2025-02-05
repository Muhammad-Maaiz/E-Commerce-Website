from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class UserWishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlisted_by')

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
