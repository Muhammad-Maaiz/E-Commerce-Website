from django.contrib import admin
from .models import Order, OrderItem, DeliveryDetail


class OrderItemInline(admin.TabularInline):  
    model = OrderItem
    extra = 0  
    max_num = 0
    can_delete = False  
    readonly_fields = ('product', 'quantity', 'price', 'item_total')  


class DeliveryDetailInline(admin.StackedInline):  
    model = DeliveryDetail
    extra = 0
    can_delete = False
    readonly_fields = ('full_name', 'email', 'address', 'city', 'postal_code', 'phone', 'notes')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tax', 'delivery_charges',  'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    fields = ('user', 'tax', 'delivery_charges', 'total_amount', 'status', 'is_verified')
    readonly_fields = ('user','tax', 'delivery_charges', 'total_amount')
    inlines = [OrderItemInline, DeliveryDetailInline]  