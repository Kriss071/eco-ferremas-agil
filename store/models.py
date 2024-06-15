from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='productos_img', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=90, unique=True)

    def __str__(self):
        return self.name