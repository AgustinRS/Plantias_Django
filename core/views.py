
from django.shortcuts import render, redirect
from core.carrito import *
from core.forms import ProductoForm, DescuentoForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

    
def home(request):
    
    producto = Producto.objects.filter(stock__lt=20)
    
    datos = {
        'producto' : producto
    }
    
    return render(request, 'core/home.html',datos)

def admin_producto(request):
    
    producto = Producto.objects.all()
    
    datos = {
        'producto' : producto
    }
    
    return render(request, 'core/admin_producto.html',datos)

def agregar_producto(request):
    
    datos = {'form':ProductoForm()}
    if request.method == "POST":
        form = ProductoForm(request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Agregado Exitosamente!."
  
    return render(request, 'core/agregar_producto.html', datos)

def modi_producto(request, id):
    
    producto = Producto.objects.get(idProducto=id)
    datos = {"form":ProductoForm(instance=producto)}
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado Exitosamente!."
            datos['form'] = form
    return render(request, 'core/modi_producto.html', datos)

    
def eliminarProducto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    messages.success(request, 'Producto Eliminado Correctamente')
    return redirect(to="admin_producto")




    
    
    
    
def plantas_Semillas(request):
    
    producto = Producto.objects.filter(categoria=1)
    
    datos = {
        'producto' : producto
    }
    
    return render(request, 'core/plantas_semillas.html',datos)

def macetas(request):
    
    producto = Producto.objects.filter(categoria=3)
    
    datos = {
        'producto' : producto
    }
    
    return render(request, 'core/macetas.html',datos)

def tierra_fertilizante(request):
    
    producto = Producto.objects.filter(categoria=4)
    
    datos = {
        'producto' : producto
    }
    
    return render(request, 'core/tierra_fertilizante.html',datos)

def accesorios(request):
    
    producto = Producto.objects.filter(categoria=2)
    
    datos = {
        'producto' : producto
    }
    
    return render(request, 'core/accesorios.html',datos)

def insecticidas(request):
    
    producto = Producto.objects.filter(categoria=5)
    
    datos = {
        'producto' : producto
    }
    
    return render(request, 'core/insecticida.html',datos)



def vista_producto(request, id):
        
    producto = Producto.objects.filter(idProducto=id)
    datos = {
        'producto' : producto
    }
    
    
     
    return render(request, 'core/vista_producto.html',datos)

    
    


# def registro(request):
#     if request.method == 'POST':
#         user = UserCreationForm(request.POST)
#         if user.is_valid():
#             user.save()
#             messages.success(request, "Usuario Registrado Correctamente!!")
#             return redirect(to="home")
#         else:
#             messages.success(request, "Usuario o Contraseña Incorrecto!!")
#             return render(request, 'core/registro.html', {'form':UserCreationForm()})
#     else:
#         return render(request, 'core/registro.html', {'form':UserCreationForm()})


def registro(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
    return render(request, 'core/registro.html', {'form':form})
     
    
 
def admin_descuento(request):
    
    descuento = Descuentos.objects.all()
    
    datos = {
        'descuento' : descuento
    }
    
    return render(request, 'core/admin_descuento.html',datos)

def agregar_descuento(request):
    
    datos = {'form':DescuentoForm()}
    if request.method == "POST":
        form = DescuentoForm(request.POST, files=request.FILES)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Agregado Exitosamente!."
  
    return render(request, 'core/agregar_descuento.html', datos)
    

        
def modi_descuento(request, id):
    
    descuento = Descuentos.objects.get(idDescuento=id)
    datos = {"form":DescuentoForm(instance=descuento)}
    if request.method == "POST":
        form = DescuentoForm(request.POST, instance=descuento)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Descuento Modificado Exitosamente!."
            datos['form'] = form
    return render(request, 'core/modi_descuento.html', datos)

def eliminarDescuento(request, id):
    descuento = Descuentos.objects.get(idDescuento=id)
    descuento.delete()
    messages.success(request, 'Descuento Eliminado Correctamente')
    return redirect(to="admin_descuento")





def c_agregar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito.c_agregar(producto)
    
    messages.success(request, 'se ha agregado Producto al carro')
    return redirect("home")



def c_eliminar(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    
    carrito.eliminar(producto)
    mensaje = messages.success(request, 'Producto Eliminado Correctamente')
    return redirect("home")

def restar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito.restar(producto)
   
    return redirect("home")

def limpiar_carro(request):
    carrito = Carrito(request)
    carrito.limpiar()
    messages.success(request, 'Productos Eliminado')
    return redirect("home")
    
    