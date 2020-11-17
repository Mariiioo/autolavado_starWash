# ARCHIVO QUE INDICA A LA API, CUAL ES EL MODELO QUE DEBE SERIALIZAR
# AL MOMENTO DE CARGAR LA API EN FORMATO JSON

# IMPORTAR LOS MODELOS QUE SE VAN A USAR
from StarWash.models import Insumo #importa la tabla de insumos
from rest_framework import serializers #importa los modelos de serializacion

# Crear una clase con el modelo a serializar
class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ["nombre", "precio", "descripcion", "stock"] #datos que se mostraran serializados

