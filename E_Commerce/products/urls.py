from django.urls import path
from .views import *

urlpatterns = [
    path('products/', products, name="products"),
    path('product-details/<int:product_id>/', product_details, name="product_details"),
]
