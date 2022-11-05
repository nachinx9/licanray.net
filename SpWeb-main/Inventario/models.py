from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    tiposUsuarios = [
        ('None', 'None'),
        ('Administrador', 'Administrador'),
        ('Usuario', 'Usuario'),
    ]
    tipoUsuario = models.CharField(choices=tiposUsuarios, default='None', max_length=50)

    class Meta:
        db_table = 'auth_user'

class Categoria(models.Model):
    tipoProducto = models.CharField(max_length=100)                   
    tipoTela = models.CharField(max_length=100)                        
    color = models.CharField(max_length=100)                          

class Producto(models.Model):
    #field id proporcionado por Django
    nombre = models.CharField(max_length=50)                         #Nombre del producto
    descripcion = models.TextField()                                  #Descripcion del producto
    categoria = models.OneToOneField(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField()                                     #Stock disponible del producto 


class Administrador(models.Model):
    rut = models.CharField(max_length=12)
    administradoruser = models.OneToOneField(User, on_delete=models.CASCADE)
