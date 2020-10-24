from django.contrib import admin
from .models import Galeria, Insumo ,Slider ,MisionVision

# Register your models here.



# Se crea una clase para dar estructura a la presentacion de las caracteristicas
class GaleriaAdmin(admin.ModelAdmin):
    list_display= ['nombre','descripcion','imagen'] # Campos que deseo ver
    search_fields= ['nombre','descripcion']
    list_per_page=10

class InsumoAdmin(admin.ModelAdmin):
    list_display= ['nombre','precio','descripcion','stock'] # Campos que deseo ver
    search_fields= ['nombre','precio','stock']
    list_per_page=10

class SliderAdmin(admin.ModelAdmin):
    list_display= ['nombre','imagen']  # Campos que deseo ver
    search_fields= ['nombre']
    list_per_page=10

class MisionVisionAdmin(admin.ModelAdmin):
    list_display= ['nombre','mision','imagenMision','vision','imagenVision']  # Campos que deseo ver
    search_fields= ['nombre','mision','vision']
    list_per_page=10


# Register para revisarlos dentro del admin de Django
admin.site.register(Galeria, GaleriaAdmin) 
admin.site.register(Insumo, InsumoAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(MisionVision, MisionVisionAdmin)


