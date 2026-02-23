from datetime import datetime

class Venta:
    _contador_id = 0

    def __init__(self, fecha: datetime, cliente: str, colaborador: str, productos: list, metodo_de_pago: str):
        Venta._contador_id += 1
        self.id = Venta._contador_id
        self.fecha = fecha
        self.cliente = cliente
        self.colaborador = colaborador
        self.productos = productos
        self.metodo_de_pago = metodo_de_pago

    @property
    def total(self):
        return sum(producto.precio for producto in self.productos)

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

