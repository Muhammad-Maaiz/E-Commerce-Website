from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from products.models import *
from .models import *

# Add products to user cart
def add_to_cart(request, product_id):
    # Only authenticated user add products to your cart
    if request.user.is_authenticated:   
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = UserCart.objects.get_or_create(user=request.user, product=product)
        if not created:
            # Product is already in cart
            return redirect('user_cart')
    return redirect('user_cart')


# Remove product from user cart
def remove_from_cart(request, product_id):
    # Only authenticated user remove products from your cart
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        UserCart.objects.filter(user=request.user, product=product).delete()
    return redirect('user_cart')


# Display all cart items
def user_cart(request):
    if request.user.is_authenticated:  # only authenticated users view the cart page
        cart_items = UserCart.objects.filter(user=request.user)
        
        # Calculate subtotal
        subtotal = sum(item.product.selling_price * item.quantity for item in cart_items)

        tax_rate = Decimal('0.03')  # Convert float to Decimal

        if not cart_items:
            delivery_charges = Decimal('0')  # Convert int to Decimal
        else:
            delivery_charges = Decimal('300')  # Convert int to Decimal

        # Calculate tax
        tax = subtotal * tax_rate

        # Calculate total
        total = subtotal + tax + delivery_charges

        context = {
            'cart_items': cart_items,
            'subtotal': subtotal,
            'tax': tax,
            'delivery_charges': delivery_charges,
            'total': total,
        }
        
        return render(request, 'cart/user_cart.html', context)
    return redirect('login')


# Increase product qunatity
def increase_quantity(request, product_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(UserCart, id=product_id, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        return redirect('user_cart')  
    return redirect('login')


# Decrease product quantity
def decrease_quantity(request, product_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(UserCart, id=product_id, user=request.user)
        if cart_item.quantity > 1:  
            cart_item.quantity -= 1
            cart_item.save()
        return redirect('user_cart')  
    return redirect('login')