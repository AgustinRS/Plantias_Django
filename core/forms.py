from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombre', 'stock', 'precio','descripcion','imagen','categoria','descuento']
        
class DescuentoForm(ModelForm):
    class Meta:
        model = Descuentos
        fields = ['idDescuento', 'nombreDescuento', 'porcetajeDescuento']
        
    