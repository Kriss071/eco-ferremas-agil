from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('catalogue', catalogue, name='catalogue'),
    
    path('cart', cart, name='cart'),
    path('cart/add/<int:id_product>', add_cart, name='add_cart'),
    path('cart/remove/<int:id_product>', remove_cart, name='remove'),
    path('cart/purchase', comfirm_purchase, name='comfirm_purchase'),
    
    path('retorno_flow', retorno_flow, name='retorno_flow'),
    path('confirmacion_flow', confirmacion_flow, name='confirmacion_flow'),
    
    path('error', error, name='error')
]