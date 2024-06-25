from django.db import models
from django.contrib.auth.models import User
from authentication import models as md

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=90)
    id_category = models.ForeignKey(Category, related_name='productos_categorias', on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='productos_img', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=90, unique=True)

    def __str__(self):
        return self.name
    
class Pedido(models.Model):
    id_user = models.ForeignKey(User, related_name='pedidos', null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField()
    id_direction= models.ForeignKey(md.Directions,related_name='direcciones', on_delete=models.CASCADE,blank=True,null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=60, null=True,blank=True)
    number= models.CharField(max_length=40, null=True,blank=True)
    postal_code = models.CharField(max_length=50, null=True,blank=True)
    comuna = models.CharField(max_length=50, null=True,blank=True)
    comentary = models.TextField(blank=True, null=True)
    email= models.EmailField(blank=True,null=True)



