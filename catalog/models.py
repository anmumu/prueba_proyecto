# Create your models here.
from django.db import models

class Lugar(models.Model):
    nombre = models.CharField(max_length=255)
    numero_lugar = models.AutoField(primary_key=True)
    nota = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='lugares/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Caja(models.Model):
    nombre = models.CharField(max_length=255)
    numero_caja = models.AutoField(primary_key=True)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='cajas/', blank=True, null=True)
    url = models.URLField()
    categoria = models.CharField(max_length=255, blank=True, null=True)
    etiqueta_qr = models.ImageField(upload_to='etiquetas_qr/', blank=True, null=True)
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre = models.CharField(max_length=255)
    numero_articulo = models.AutoField(primary_key=True)
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    unidades = models.IntegerField(blank=True, null=True)
    fecha_compra = models.CharField(max_length=255, blank=True, null=True)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    en_uso = models.BooleanField(default=False)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    nota = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre