from django.db import models
from Inventario.models import User, Producto

class Cliente(models.Model):
    usuariouser = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)              #nombre del cliente
    apellido = models.CharField(max_length=30)            #apellido del cliente
    rut = models.CharField(max_length=12)                 #Rut del cliente
    telefono = models.CharField(max_length=14)            #Telefono del cliente
    email = models.EmailField()                           #email del cliente   

class CarritodeCompra(models.Model):
    #field id proporcionado por Django
    usuario = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()        #Cantidad del producto a prestamo

class Direccion(models.Model):
    usuario = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    calle = models.CharField(max_length=30)               #Calle con numero
    calle2 = models.CharField(max_length=30)              #Casa, depto, etc
    comuna = models.CharField(max_length=100)             #Comuna
    region = models.CharField(max_length=100)             #Region
    cPostal = models.IntegerField()         #Codigo postal

class Pedido(models.Model):
    usuario = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    #field id proporcionado por Django
    fPrestamo = models.DateTimeField()      #Fecha de prestamo del pedido
    fDevolucion = models.DateTimeField()       #Fecha en la que se debe devolver el pedido
    estado = models.CharField(max_length=100)             #Estado en el que se encuentra el pedido (Entregado o moroso)
    

class DetallePedido(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE)            #Producto
    cantidad = models.IntegerField()        #Cantidad de productos

