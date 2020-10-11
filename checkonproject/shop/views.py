from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    return render(request, 'index.html')

def product(request):
    products = Product.objects
    return render(request, 'index.html', {'products' : products})


