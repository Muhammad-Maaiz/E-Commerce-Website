from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contact-us/', contact_us, name="contact_us"),
    path('about-us/', about_us, name="about_us"),
]