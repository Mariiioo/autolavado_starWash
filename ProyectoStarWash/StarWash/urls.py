from django.contrib import admin
from django.urls import path,include
from .views import index,galeria,formulario,conocenos,ubicacion, insumos, login, logout_vista, adminInsumo, eliminar_insumo

urlpatterns = [
    path('',index,name="INDEX"),
    path('galeria/',galeria,name="GALERIA"),
    path('formulario/',formulario,name="FORMULARIO"),
    path('conocenos/',conocenos,name="CONOCENOS"),
    path('ubicacion/',ubicacion,name="UBICACION"),
    path('registro_insumos/', insumos, name='INSUMOS'),
    path('login/', login, name="LOGIN"),
    path('logout_vista/', logout_vista, name="LOGOUT"),
    path('administracion_insumos/', adminInsumo, name='ADMIN_INSUMO'),
    path('eliminar_insumo/<id>/', eliminar_insumo, name="ELIM_INSUMO")
]
