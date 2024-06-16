from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('catalogue', catalogue, name='catalogue'),
    
    path('cart', cart, name='cart'),
    path('cart/add/<int:id_product>', add_cart, name='add_cart'),
    path('cart/remove/<int:id_product>', remove_cart, name='remove'),
    
    path('error', error, name='error')
]