from django import forms
from authentication import models
from .models import *

class ComfirmPurchaseForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    phone = forms.CharField(label='Teléfono', max_length=20)
    street = forms.CharField(label='Calle', max_length=100)
    number = forms.CharField(label='Número', max_length=10)
    postal_code = forms.CharField(label='Código Postal', max_length=10)
    comentary = forms.CharField(label='Comentario', widget=forms.Textarea)
    email = forms.EmailField(label='Correo Electrónico')
    
class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['id_direction', 'phone']
        labels={
            'id_direction': 'Direcciones Guardadas',
            'phone': 'telefono'
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PedidoForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['id_direction'].queryset = models.Directions.objects.filter(id_usuario=user)
        self.fields['id_direction'].required = True