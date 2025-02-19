from django.contrib import admin
from .models import Category, Product, ProductAttribute, Review

# Register Category Model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Show ID and Name in admin panel
    search_fields = ('name',)      # Search by name

# Inline Formset for ProductAttribute (for dynamic attributes like Color, Size, etc.)
class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1  # Number of empty fields to show for adding new attributes

# Register Product Model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'cost_price', 'selling_price', 'quantity', 'created_at', 'updated_at']
    inlines = [ProductAttributeInline]

    fieldsets = (
        (None, {
            'fields': ('name', 'cost_price', 'selling_price', 'quantity', 'image1','image2', 'image3', 'description', 'category', 'is_trending', 'is_featured')
        }),
    )

admin.site.register(Review)