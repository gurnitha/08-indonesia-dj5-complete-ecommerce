# src/app/shop/urls.py

# Django and third parties modules
from django.urls import path

# Local
from app.shop.views import welcome_view

app_name = 'shop'

urlpatterns = [
    path("", welcome_view),
]