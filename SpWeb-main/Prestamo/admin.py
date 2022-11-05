from django.contrib import admin

from Prestamo.models import Cliente, CarritodeCompra, Direccion, Pedido, DetallePedido

admin.site.register(Cliente)
admin.site.register(CarritodeCompra)
admin.site.register(Direccion)
admin.site.register(Pedido)
admin.site.register(DetallePedido)