from django.shortcuts import render, redirect
from .models import *
from .cart import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

def catalogue(request):
    category = request.GET.get('category', 0)
    products = Product.objects.all()
    categories = Category.objects.all()
    
    if category:
        products = products.filter(id_category=category)
        
    context = {
        'products': products,
        'categories': categories,
        'categoria_id': category
    }
    
    return render(request, 'catalogue.html', context)

# === Cart ===
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
