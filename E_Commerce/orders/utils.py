from decimal import Decimal

def calculate_order_summary(items):
    """ Helper function to calculate order totals """
    subtotal = sum(item.product.selling_price * item.quantity for item in items)
    tax_rate = Decimal('0.03')
    tax = subtotal * tax_rate
    delivery_charges = Decimal('300')
    total_amount = subtotal + tax + delivery_charges
    return subtotal, tax, delivery_charges, total_amount