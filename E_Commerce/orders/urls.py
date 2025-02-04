from django.urls import path
from .views import *

urlpatterns = [
    path("confirm-order/", confirm_order, name="confirm_order"),
    path("order-success/", order_success, name="order_success"),
    path("buy-now/<int:product_id>/", buy_now, name="buy_now"),
    path("confirm-buy-now/<int:product_id>/", confirm_buy_now, name="confirm_buy_now"),
]
