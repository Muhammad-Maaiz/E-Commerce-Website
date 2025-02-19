from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the category (e.g., Phone, Clothes)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    quantity = models.IntegerField(default=0)
    image1 = models.ImageField(upload_to="products/")
    image2 = models.ImageField(upload_to="products/", null=True, blank=True)
    image3 = models.ImageField(upload_to="products/", null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="products")
    is_trending = models.BooleanField(default=False)   
    is_featured = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    def __str__(self):
        return self.name
    
    def average_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum([review.rating for review in ratings]) / ratings.count(), 1)
        return 0

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # 1 to 5
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')  # Ensure a user can only review a product once

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.rating} stars)"


# Dynamic Attributes for Products
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')
    key = models.CharField(max_length=50)  # e.g., Color, Size, Brand
    value = models.CharField(max_length=250)  # e.g., Red, Large, Nike

    def __str__(self):
        return f"{self.key}: {self.value}"
