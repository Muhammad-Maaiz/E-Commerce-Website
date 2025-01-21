from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def products(request):
    all_products = Product.objects.all()

    context = {
        'products': all_products
    }
    return render(request, 'products/products.html', context)


from django.shortcuts import get_object_or_404, render

# Display all product details on the product detail page
def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    attributes = product.attributes.all()

    context = {
        "product": product,
        "attributes": attributes,
    }

    return render(request, "products/product_detail.html", context)
