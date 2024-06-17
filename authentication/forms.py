from django import forms
from allauth.account.forms import *
from store import models

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Nombre', required=True)
    last_name = forms.CharField(max_length=30, label='Apellido', required=True)

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Ingrese su correo'
        self.fields['username'].widget.attrs['placeholder'] = 'Ingrese nombre de usuario'
        self.fields['password1'].widget.attrs['placeholder'] = 'Ingrese contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Ingrese nuevamente su contraseña'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ingrese su nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ingrese su apellido'

    def save(self, request):
        # Asegúrate de llamar al método save de la clase padre
        user = super(CustomSignupForm, self).save(request)

        # Añade tu propio procesamiento aquí
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        # Debes devolver el resultado original
        return user


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget.attrs['placeholder'] = 'Ingresa tu usuario o correo electrónico'
        self.fields['password'].widget.attrs['placeholder'] = 'Ingresa tu contraseña'
        self.fields['remember'].widget.attrs['class'] = 'checkbox__recuerdame'
        self.fields['login'].label = "Usuario"

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email']

        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico'
        }
        
        
class CategoriesForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['name']