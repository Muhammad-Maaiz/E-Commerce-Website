from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import UserCart
from products.models import Product
from .models import Order, OrderItem, DeliveryDetail
from decimal import Decimal
from .utils import calculate_order_summary

@login_required(login_url="login")
def confirm_order(request):
    cart_items = UserCart.objects.filter(user=request.user)
    
    if not cart_items.exists():
        return redirect("user_cart")

    subtotal, tax, delivery_charges, total_amount = calculate_order_summary(cart_items)

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        postal_code = request.POST.get("postal_code")
        phone = request.POST.get("phone")
        notes = request.POST.get("notes", "")

        order = Order.objects.create(
            user=request.user,
            tax=Decimal(tax),
            delivery_charges=delivery_charges,
            total_amount=Decimal(total_amount),
        )

        DeliveryDetail.objects.create(
            order=order,
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            postal_code=postal_code,
            phone=phone,
            notes=notes,
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=Decimal(item.product.selling_price),
                item_total=Decimal(item.quantity * item.product.selling_price),
            )

        cart_items.delete()

        return redirect("order_success")

    context = {
        "cart_items": cart_items,
        "subtotal": subtotal,
        "tax": tax,
        "delivery_charges": delivery_charges,
        "total_amount": total_amount,
    }
    return render(request, "orders/confirm_order.html", context)


@login_required(login_url="login")
def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.session["product_id"] = product.id
    return redirect("confirm_buy_now", product.id)


@login_required(login_url="login")
def confirm_buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Calculate order summary for a single product
    subtotal = product.selling_price  
    tax_rate = Decimal('0.03')
    tax = subtotal * tax_rate
    delivery_charges = Decimal('300')
    total_amount = subtotal + tax + delivery_charges

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        city = request.POST.get("city")
        postal_code = request.POST.get("postal_code")
        phone = request.POST.get("phone")
        notes = request.POST.get("notes", "")

        order = Order.objects.create(
            user=request.user,
            tax=Decimal(tax),
            delivery_charges=delivery_charges,
            total_amount=Decimal(total_amount),
        )

        DeliveryDetail.objects.create(
            order=order,
            full_name=full_name,
            email=email,
            address=address,
            city=city,
            postal_code=postal_code,
            phone=phone,
            notes=notes,
        )

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=1,
            price=Decimal(product.selling_price),
            item_total=subtotal,
        )

        return redirect("order_success")

    context = {
        "cart_items": [{
            "product": product,
            "quantity": 1
        }],
        "subtotal": subtotal,
        "tax": tax,
        "delivery_charges": delivery_charges,
        "total_amount": total_amount,
    }
    return render(request, "orders/confirm_order.html", context)



@login_required(login_url="login")
def order_success(request):
    return render(request, "orders/order_success.html")
