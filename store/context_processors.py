from .cart import Cart

def cart(request):
    cart = Cart(request)
    total = cart.total()
    ivaTotal = total * 0.19
    neto = total * 0.81
    return {'cart': cart, 'total': total, 'ivaTotal': ivaTotal, 'neto': neto}
