from django.contrib import admin

from Inventario.models import Categoria, Producto, User, Administrador

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(User)
admin.site.register(Administrador)