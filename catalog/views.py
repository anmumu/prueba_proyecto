from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Lugar, Caja, Articulo
from .forms import LugarForm, CajaForm, ArticuloForm

# Vistas para Lugar
class LugarListView(ListView):
    model = Lugar
    template_name = 'catalog/lugar_list.html'
    context_object_name = 'lugares'

class LugarDetailView(DetailView):
    model = Lugar
    template_name = 'catalog/lugar_detail.html'

class LugarCreateView(CreateView):
    model = Lugar
    form_class = LugarForm
    template_name = 'catalog/lugar_form.html'
    success_url = reverse_lazy('lugar_list')

class LugarUpdateView(UpdateView):
    model = Lugar
    form_class = LugarForm
    template_name = 'catalog/lugar_form.html'
    success_url = reverse_lazy('lugar_list')

class LugarDeleteView(DeleteView):
    model = Lugar
    template_name = 'catalog/lugar_confirm_delete.html'
    success_url = reverse_lazy('lugar_list')

# Vistas para Caja
class CajaListView(ListView):
    model = Caja
    template_name = 'catalog/caja_list.html'
    context_object_name = 'cajas'

class CajaDetailView(DetailView):
    model = Caja
    template_name = 'catalog/caja_detail.html'

class CajaCreateView(CreateView):
    model = Caja
    form_class = CajaForm
    template_name = 'catalog/caja_form.html'
    success_url = reverse_lazy('caja_list')

class CajaUpdateView(UpdateView):
    model = Caja
    form_class = CajaForm
    template_name = 'catalog/caja_form.html'
    success_url = reverse_lazy('caja_list')

class CajaDeleteView(DeleteView):
    model = Caja
    template_name = 'catalog/caja_confirm_delete.html'
    success_url = reverse_lazy('caja_list')

# Vistas para Articulo
class ArticuloListView(ListView):
    model = Articulo
    template_name = 'catalog/articulo_list.html'
    context_object_name = 'articulos'

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'catalog/articulo_detail.html'

class ArticuloCreateView(CreateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'catalog/articulo_form.html'
    success_url = reverse_lazy('articulo_list')

class ArticuloUpdateView(UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'catalog/articulo_form.html'
    success_url = reverse_lazy('articulo_list')

class ArticuloDeleteView(DeleteView):
    model = Articulo
    template_name = 'catalog/articulo_confirm_delete.html'
    success_url = reverse_lazy('articulo_list')