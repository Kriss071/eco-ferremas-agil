class Cart():
    def __init__(self, request):
        self.session = request.session
        # Busca el carrito en la session
        cart = self.session.get('cart')
        
        # Si no lo encuentra, lo crea
        if not cart:
            cart = self.session['cart'] = {}
            
        self.cart = cart
        
    # Agrega productos en el carrito
    def add(self, product, quantity=1):
        product_id = str(product.id)
        
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
            self.cart[product_id]['total_price'] = float(product.price) * self.cart[product_id]['quantity']

        else:
            self.cart[product_id] = {
                'name' : product.name,
                'brand': product.brand,
                'price': float(product.price),  # Convertir Decimal a float
                'code': product.code,
                'quantity': quantity,
                'total_price': float(product.price) * quantity
            }
            
        self.session.modified = True
        
    # Elimina producto del carrito
    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            if self.cart[product_id]['quantity'] > 1:
                self.cart[product_id]['quantity'] -= 1
                self.cart[product_id]['total_price'] -= float(self.cart[product_id]['price'])
            else:
                del self.cart[product_id]
            self.session.modified = True
      
    # Limpia el carrito
    def clear(self):
        self.session['session_key'] = {}
        self.session.modified = True
        
    # Calcula el total    
    def total(self):
        total = sum(item_info['total_price'] for item_info in self.cart.values())
        return total
    
    