from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from orders.models import OrderItem

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products/products.html', {'products': all_products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    attributes = product.attributes.all()
    reviews = product.reviews.all().order_by('-created_at')
    avg_rating = product.average_rating()
    user_review = None
    verified_order = False  # Default False

    if request.user.is_authenticated:
        user_review = product.reviews.filter(user=request.user).first()  
        verified_order = OrderItem.objects.filter(order__user=request.user, order__is_verified=True, product=product).exists()

    context = {
        "product": product,
        "attributes": attributes,
        "reviews": reviews,
        "avg_rating": avg_rating,
        "user_review": user_review,
        "verified_order": verified_order,
    }
    return render(request, "products/product_detail.html", context)

@login_required
def add_review(request, product_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            rating = int(data.get("rating"))
            review_text = data.get("review_text", "").strip()

            if rating < 1 or rating > 5:
                return JsonResponse({"error": "Invalid rating"}, status=400)

            product = get_object_or_404(Product, id=product_id)

            review, created = Review.objects.update_or_create(
                product=product,
                user=request.user,
                defaults={"rating": rating, "review_text": review_text}
            )

            return JsonResponse({"message": "Review submitted successfully", "rating": rating, "review_text": review_text})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid data"}, status=400)
    
    return JsonResponse({"error": "Invalid request"}, status=400)