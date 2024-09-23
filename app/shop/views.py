# src/app/shop/views.py

# Django and third parties modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome_view(request):
	return HttpResponse('Selamat Datang di INGShop')