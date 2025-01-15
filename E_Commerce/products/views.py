from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
# def products(request):
#     products = Product.objects.prefetch_related('attributes').all()

#     context = {
#         "products": products,
#     }

#     return render(request, "products/home.html", context)

def products(request):
    all_products = Product.objects.all()

    context = {
        'products': all_products
    }
    return render(request, 'products/products.html', context)

