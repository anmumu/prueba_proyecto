from django import forms
from .models import Lugar, Caja, Articulo

class LugarForm(forms.ModelForm):
    class Meta:
        model = Lugar
        fields = ['nombre', 'nota', 'imagen']

class CajaForm(forms.ModelForm):
    class Meta:
        model = Caja
        fields = ['nombre', 'lugar', 'imagen', 'url', 'categoria', 'etiqueta_qr', 'nota']

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre', 'caja', 'imagen', 'unidades', 'fecha_compra', 'precio_compra', 'en_uso', 'categoria', 'nota']