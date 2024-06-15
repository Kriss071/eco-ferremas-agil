from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def catalogue(request):
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    
    return render(request, 'catalogue.html', context)