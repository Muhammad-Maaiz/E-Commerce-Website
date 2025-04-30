from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Order
from django.conf import settings


@receiver(post_save, sender=Order)
def send_order_confirm_email(sender, instance, created, **kwargs):
    if created:  
        user_email = instance.user.email
        user_name = instance.user.username
        order_id = instance.id

        # HTML Email Template Render
        html_message = render_to_string("orders/order_confirmation_email.html", {
            "username": user_name,
            "order_id": order_id
        })

        plain_message = strip_tags(html_message)  

        send_mail(
            subject="Cartobuz - Order Confirmation",
            message=plain_message,  
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user_email],
            html_message=html_message,  
            fail_silently=False,
        )
        print("Successfully Send email")
    else:
        print("Not Send email Successfully")
