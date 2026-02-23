from .persona import Persona

class Cliente(Persona):
    
    def __init__(self, nombre: str, apellido: str, telefono: str, correo: str, historialDeCompras: list, puntos: int):
        super().__init__(nombre, apellido, telefono, correo)
        self._historialDeCompras = historialDeCompras
        self._puntos = puntos
        
    @property
    def historialDeCompras(self):
        return self._historialDeCompras
    
    @historialDeCompras.setter
    def historialDeCompras(self, historialDeCompras: list):
        self._historialDeCompras = historialDeCompras
    
    @property
    def puntos(self):
        return self._puntos
    
    @puntos.setter
    def puntos(self, puntos: int):
        self._puntos = puntos