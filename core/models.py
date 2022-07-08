from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=30)

    def __str__(self) :
        return self.nombreCategoria

class Descuentos(models.Model):
    idDescuento = models.IntegerField(primary_key=True)
    nombreDescuento = models.CharField(max_length=30)
    porcetajeDescuento = models.IntegerField()

    def __str__(self) :
        return self.nombreDescuento


class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    stock = models.IntegerField()
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="productos",null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descuento = models.ForeignKey(Descuentos , on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self) :
        return self.nombre
    
    
    
    
