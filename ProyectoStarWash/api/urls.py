# SE CREO YA QUE NO ESTABA

from django.conf.urls import url # Importa direcciones url
from api import views # Importa todas las views
from rest_framework.urlpatterns import format_suffix_patterns # Para poner sufijos a la url

# Creacion de la url
# PARA HACER ELEVADO = alt + 94 ^ 
urlpatterns = [
    # Definir la ruta empieza con ^ y termina con $
    url(r'^api/lista_insumos/$',views.ListaInsumosViewSet.as_view()), # muestra todos los insumos
    url(r'^api/insumos/$', views.InsumosViewSet.as_view()), # lleva a la api donde se ve y guarda
    url(r'^api/insumos_nombre/(?P<nombre>.+)/$', views.InsumoFiltroNombreViewSet.as_view()), # solo mostrara el insumo que se ingrese
    url(r'^api/insumos_precio/(?P<precio>[0-9]+)/$', views.InsumoFiltroPrecioViewSet.as_view()), # solo mostraran los precios
]