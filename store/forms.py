from django import forms

class ComfirmPurchaseForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=100)
    phone = forms.CharField(label='Teléfono', max_length=20)
    street = forms.CharField(label='Calle', max_length=100)
    number = forms.CharField(label='Número', max_length=10)
    postal_code = forms.CharField(label='Código Postal', max_length=10)
    comentary = forms.CharField(label='Comentario', widget=forms.Textarea)
    email = forms.EmailField(label='Correo Electrónico')