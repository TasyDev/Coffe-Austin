from Producto import Producto

class Cafe(Producto):
    def __init__(self, nombre: str, precio: float, descripcion: str, disponible: bool, tipo: str, temperatura: str, tamaño: str):
        super().__init__(nombre, precio, descripcion, disponible)
        self.tipo = tipo
        self.temperatura = temperatura
        self.tamaño = tamaño

    def prepararCafe(self):
        print(f"Preparando {self.nombre}...")
        print(f"Tipo: {self.tipo}")
        print(f"Temperatura: {self.temperatura}")
        print(f"Tamaño: {self.tamaño}")
        print("Listo!")
    
