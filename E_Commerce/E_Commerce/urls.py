from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("authentication.urls")),
    path('', include('home.urls')), 
    path('', include("products.urls")),
    path('', include('wishlist.urls')),
    path('', include('cart.urls')),
    path('', include('orders.urls')),
]

# Add media settings
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)