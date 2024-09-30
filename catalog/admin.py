from django.contrib import admin

# Register your models here.
from .models import Lugar, Caja, Articulo

admin.site.register(Lugar)
admin.site.register(Caja)
admin.site.register(Articulo)
