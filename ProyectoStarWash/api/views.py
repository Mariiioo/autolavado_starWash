from django.shortcuts import render
from rest_framework import generics # Importa las vistas generias, que son templates ya diseñadas
from StarWash.models import Insumo, Contacto# Importa la tabla insumos
from .serializers import InsumoSerializer, ContactoSerializer # Importa la clase serializer creada en la ap API 

# Creacion de la vista Insumos: NORMA DEBE TENER ViewSet(una vista generia.ListApiView)}
# MUESTRA TODOS LOS DATOS DE LOS INSUMOS
class ListaInsumosViewSet(generics.ListAPIView):
    queryset = Insumo.objects.all() # Ver todos los insumos
    serializer_class = InsumoSerializer

# OPCION DE CREAR Y LISTA EN UNA VISTA GENERICA LOS INSUMOS
class InsumosViewSet(generics.ListCreateAPIView):
    queryset = Insumo.objects.all() # Ver todos los datos
    serializer_class = InsumoSerializer # Seran serializados a la clase creada

# FILTRAR Y BUSCAR EL NOMBRE DEL INSUMO
class InsumoFiltroNombreViewSet(generics.ListAPIView):
    serializer_class = InsumoSerializer
    def get_queryset(self):
        nombreUrl = self.kwargs['nombre']
        return Insumo.objects.filter(nombre = nombreUrl)

# FILTRAR Y BUSCAR EL PRECIO DEL INSUMO
class InsumoFiltroPrecioViewSet(generics.ListAPIView):
    serializer_class = InsumoSerializer
    def get_queryset(self):
        precioUrl = self.kwargs['precio']
        return Insumo.objects.filter(precio = precioUrl)

 # MUESTRA TODOS LOS DATOS DE LOS CONTACTO
class ListaContactoViewSet(generics.ListAPIView):
    queryset = Contacto.objects.all() # Ver todos los contactos
    serializer_class = ContactoSerializer

# OPCION DE CREAR Y LISTA EN UNA VISTA GENERICA LOS CONTACTOS
class ContactosViewSet(generics.ListCreateAPIView):
    queryset = Contacto.objects.all() # Ver todos los datos
    serializer_class = ContactoSerializer # Seran serializados a la clase creada