from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Directions(models.Model):
    id_usuario = models.ForeignKey(User, related_name='direcciones', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    comuna = models.CharField(max_length=60)
    calle = models.CharField(max_length=60)
    numero= models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=50)
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre