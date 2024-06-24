from django.shortcuts import render, redirect
from .models import *
from .cart import *
from .forms import *
from .flow_utils import *

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

def comfirm_purchase(request):
    cart = Cart(request)
    
    if not cart.cart:
        context = {
            'No se pudo obtener el carrito'
        }
        return redirect(error, context)
    
    if request.method == 'POST':
        form = ComfirmPurchaseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            total = cart.total()
            data['total_price'] = total
            
            response = create_payment(request, data['name'], total, data['email'])

            url = response['url']
            token = response['token']
            payment_url = f"{url}?token={token}"
            
            cart.clear() 
            return redirect(payment_url)
            
                
    else:
        form = ComfirmPurchaseForm()
        
        context = {
            'form': form
        }
        
        return render(request, 'cart/confirm_purchase.html', context)
    
def retorno_flow(request):
    return redirect(index)

def confirmacion_flow(request):
    return redirect(catalogue)
    
def error(request, context):
    return render(request, 'error.html', context)
