from .producto import Producto

class Comida(Producto):
    def __init__(self, nombre: str, precio: float, descripcion: str, disponible: bool, categoria: str, calorias: int):
        super().__init__(nombre, precio, descripcion, disponible)
        self.categoria = categoria
        self.calorias = calorias
    
    def haciendoComida(self):
        print(f"Haciendo {self.nombre}...")
        print(f"Categoria: {self.categoria}")
        print(f"Calorias: {self.calorias}")
        print("Listo!")