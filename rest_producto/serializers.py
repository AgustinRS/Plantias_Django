from dataclasses import field
from rest_framework import serializers
from core.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombre', 'stock', 'precio', 'descripcion', 'imagen', 'categoria', 'descuento']
            
            
            
"""serializer agregado"""