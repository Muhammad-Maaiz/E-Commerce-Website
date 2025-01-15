from django.shortcuts import render, redirect
from products.models import *
from .models import *
from django.contrib.auth.decorators import login_required

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

        print(full_name, email, message, request.user)
        if not request.user.is_authenticated:
            return render(request, 'home/contact_us.html', {"error": "You need to log in to submit the form!"})
            # return redirect('login')  # Redirect to login page if user is not logged in

        save_form_info = ContactForm.objects.create(
            user = request.user,
            full_name = full_name,
            email = email,
            message = message
        )
        return redirect('home')

    return render(request, 'home/contact_us.html')


def about_us(request):
    return render(request, 'home/about_us.html')