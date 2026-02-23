from .persona import Persona

class Cliente(Persona):
    
    def __init__(self, nombre: str, apellido: str, telefono: str, correo: str):
        super().__init__(nombre, apellido, telefono, correo)
        
    def comprar(self, producto: str):
        print(f"El cliente {self.nombre} {self.apellido} ha comprado {producto}")
    
    def pagar(self, monto: float):
        print(f"El cliente {self.nombre} {self.apellido} ha pagado {monto}")