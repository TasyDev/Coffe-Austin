from .venta import Venta

class Tienda:
    def __init__(self, clientes: list, colaboradores: list, menu: list, ventas: list):
        self.clientes = clientes
        self.colaboradores = colaboradores
        self.menu = menu
        self.ventas = ventas
    
    def agregar_cliente(self, cliente: str):
        self.clientes.append(cliente)
    
    def eliminar_cliente(self, cliente: str):
        self.clientes.remove(cliente)
    
    def agregar_colaborador(self, colaborador: str):
        self.colaboradores.append(colaborador)
    
    def eliminar_colaborador(self, colaborador: str):
        self.colaboradores.remove(colaborador)
    
    def agregar_producto(self, producto: str):
        self.menu.append(producto)
    
    def eliminar_producto(self, producto: str):
        self.menu.remove(producto)
    
    def agregar_venta(self, venta: Venta):
        self.ventas.append(venta)
    
    def eliminar_venta(self, venta: Venta):
        self.ventas.remove(venta)
    
    def obtener_ventas(self):
        return self.ventas