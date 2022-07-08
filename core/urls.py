
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

urlpatterns = [
    path('', home, name="home"),
    path('agregar_producto', agregar_producto , name="agregar_producto"),
    path('modi_producto/<id>', modi_producto , name="modi_producto"),
    path('admin_producto',admin_producto , name="admin_producto"),
    path('eliminarProducto/<id>', eliminarProducto, name="eliminarProducto"),
    path('registro', registro, name="registro"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='core/logout.html'), name="logout"),
    path('plantas_semillas', plantas_Semillas , name="plantas_semillas"),
    path('macetas', macetas , name="macetas"),
    path('tierra_fertilizante', tierra_fertilizante , name="tierra_fertilizante"),
    path('accesorios', accesorios , name="accesorios"),
    path('insecticidas',  insecticidas , name="insecticidas"),
    path('vista_producto/<id>',   vista_producto , name="vista_producto"),
    path('admin_descuento',admin_descuento , name="admin_descuento"),
    path('agregar_descuento', agregar_descuento , name="agregar_descuento"),
    path('modi_descuento/<id>', modi_descuento , name="modi_descuento"),
    path('eliminarDescuento/<id>', eliminarDescuento, name="eliminarDescuento"),
    
    path('c_agregar/<id>', c_agregar_producto, name="add"),
    path('eliminar/<id>', c_eliminar, name="del"),
    path('restar/<id>', restar_producto, name="sub"),
    path('limpiar', limpiar_carro, name="CLS"),
    

]

