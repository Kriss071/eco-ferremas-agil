from django.db import models

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