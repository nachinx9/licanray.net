import graphene
from graphene_django import DjangoObjectType

from Inventario.models import Categoria, Producto
from Prestamo.models import Cliente, Usuario, CarritodeCompra, Direccion, Pedido, DetallePedido

class CategoriaType(DjangoObjectType):
    class Meta:
        model = Categoria
        fields = ("tipoProducto")

class ProductoType(DjangoObjectType):
    class Meta:
        model = Producto
        fields = ("idProducto", "nombre", "descripcion", "stock")

class ClienteType(DjangoObjectType):
    class Meta:
        model = Cliente
        fields = ("nombre", "apellido", "rut", "telefono", "email")

class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario
        fields = ("contraseña", "fechaCreacion")

class CarritodeCompraType(DjangoObjectType):
    class Meta:
        model = CarritodeCompra
        fields = ("idCarrito", "producto", "cantidad")

class DireccionType(DjangoObjectType):
    class Meta:
        model = Direccion
        fields = ("calle", "calle2", "comuna", "region", "cPostal")

class PedidoType(DjangoObjectType):
    class Meta:
        model = Pedido
        fields = ("idPedido", "fPrestamo", "fDevolucion", "estado")

class DetallePedidoType(DjangoObjectType):
    class Meta:
        model = DetallePedido
        fields = ("producto", "vUnidad", "cantidad")


'''class Query(graphene.ObjectType):
    all_ingredients = graphene.List(ProductoType)
    category_by_name = graphene.Field(CategoriaType, name=graphene.String(required=True))

    def resolve_all_ingredients(root):
        # We can easily optimize query count in the resolve method
        return Producto.objects.select_related("categoria").all()

    def resolve_category_by_name(root, name):
        try:
            return Categoria.objects.get(name=name)
        except Categoria.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)'''