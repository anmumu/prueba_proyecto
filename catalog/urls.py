from django.urls import path
from . import views

urlpatterns = [
    # URLs para Lugar
    path('lugares/', views.LugarListView.as_view(), name='lugar_list'),
    path('lugar/<int:pk>/', views.LugarDetailView.as_view(), name='lugar_detail'),
    path('lugar/nuevo/', views.LugarCreateView.as_view(), name='lugar_create'),
    path('lugar/<int:pk>/editar/', views.LugarUpdateView.as_view(), name='lugar_update'),
    path('lugar/<int:pk>/eliminar/', views.LugarDeleteView.as_view(), name='lugar_delete'),

    # URLs para Caja
    path('cajas/', views.CajaListView.as_view(), name='caja_list'),
    path('caja/<int:pk>/', views.CajaDetailView.as_view(), name='caja_detail'),
    path('caja/nueva/', views.CajaCreateView.as_view(), name='caja_create'),
    path('caja/<int:pk>/editar/', views.CajaUpdateView.as_view(), name='caja_update'),
    path('caja/<int:pk>/eliminar/', views.CajaDeleteView.as_view(), name='caja_delete'),

    # URLs para Articulo
    path('articulos/', views.ArticuloListView.as_view(), name='articulo_list'),
    path('articulo/<int:pk>/', views.ArticuloDetailView.as_view(), name='articulo_detail'),
    path('articulo/nuevo/', views.ArticuloCreateView.as_view(), name='articulo_create'),
    path('articulo/<int:pk>/editar/', views.ArticuloUpdateView.as_view(), name='articulo_update'),
    path('articulo/<int:pk>/eliminar/', views.ArticuloDeleteView.as_view(), name='articulo_delete'),
]
