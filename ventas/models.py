from django.db import models
from django.utils import timezone

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, max_length=7)
    nombre = models.CharField(default='', max_length=100)
    foto = models.ImageField(upload_to='media/imagenes/')
    marca = models.CharField(default='', max_length=50)
    precio_unitario = models.FloatField(default=0)
    existencias = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    
class Usuario(models.Model):
    dpi = models.TextField()
    nombre = models.TextField()
        
    def __str__(self):
        return self.nombre