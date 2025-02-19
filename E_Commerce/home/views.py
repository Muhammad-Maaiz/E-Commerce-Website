from django.shortcuts import render, redirect
from products.models import *
from orders.models import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

# @login_required(login_url='login')
def home(request):
    # Get all featured products
    featured_products = Product.objects.filter(is_featured=True)
    
    # Get all Trending products
    trending_products = Product.objects.filter(is_trending=True)

    context = {
        'featured_products': featured_products,
        'trending_products': trending_products,
        }

    return render(request, "home/home.html", context)


def contact_us(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone_number = request.POST.get('phone_number')


        if not request.user.is_authenticated:
            return render(request, 'home/contact_us.html', {"error": "You need to log in to submit the form!"})
        
        if not len(phone_number) == 11:
            return render(request, 'home/contact_us.html', {"error": "Please enter correct phone number."})


        # Save form data to the database
        ContactForm.objects.create(
            user=request.user,
            full_name=full_name,
            phone_number=phone_number,
            email=email,
            message=message
        )
        return redirect('contact_us')

    return render(request, 'home/contact_us.html')


def about_us(request):
    return render(request, 'home/about_us.html')



def search(request):
    search_query = request.GET.get("search", "")  # Get search query from URL
    products = Product.objects.filter(
        Q(name__icontains=search_query) |
        Q(category__name__icontains=search_query) |
        Q(selling_price__icontains=search_query)
    )

    return render(request, "home/search_results.html", {"products": products, "query": search_query})


@login_required(login_url="login")
def user_profile(request):
    user = request.user
    orders = Order.objects.filter(user=user).order_by('-created_at') 

    context = {
        "user": user,
        "orders": orders}

    return render(request, "home/user_profile.html", context)
