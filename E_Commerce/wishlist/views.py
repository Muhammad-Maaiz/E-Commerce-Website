from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import UserWishlist

# Add to Wishlist
def add_to_wishlist(request, product_id):
    # Only authenticated user add products to your wishlists
    if request.user.is_authenticated:   
        product = get_object_or_404(Product, id=product_id)
        wishlist_item, created = UserWishlist.objects.get_or_create(user=request.user, product=product)
        if not created:
            # Product is already in wishlist
            return redirect('wishlist')
    return redirect('wishlist')

# Remove from Wishlist
def remove_from_wishlist(request, product_id):
    # Only authenticated user remove products from your wishlists
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        UserWishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')

# Display Wishlist
def display_user_wishlist(request):
    if request.user.is_authenticated:   # only authenticated users view wishlists page
        wishlist = UserWishlist.objects.filter(user=request.user)

        context = {'wishlist': wishlist}

        return render(request, 'wishlist/wishlist.html', context)
    return redirect('login')
