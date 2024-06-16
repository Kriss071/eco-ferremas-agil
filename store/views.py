from django.shortcuts import render, redirect
from .models import *
from .cart import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def catalogue(request):
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    
    return render(request, 'catalogue.html', context)

def cart(request):
    return render(request, 'cart/cart.html')

def add_cart(request, id_product):
    cart = Cart(request)    
    product = Product.objects.get(id=id_product)
    
    if product:
        cart.add(product)
        return redirect('cart')
    else:
        context = {
            'error_message': 'Hubo un error al encontrar el producto'
        }
        return redirect('error', context = context)
    
def remove_cart(request, id_product):
    cart = Cart(request)
    cart.remove(id_product)
    return redirect('cart')

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart')

    
def error(request, context):
    return render(request, 'error.html', context)
