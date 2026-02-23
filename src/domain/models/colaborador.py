from .persona import Persona

class Colaborador(Persona):
    def __init__(self, nombre: str, apellido: str, telefono: str, correo: str, horaDeLlegada: str, horaDeSalida: str):
        super().__init__(nombre, apellido, telefono, correo)
        self._horaDeLlegada = horaDeLlegada
        self._horaDeSalida = horaDeSalida    
    
    @property
    def horaDeLlegada(self):
        horaDeLlegada = self._horaDeLlegada
        return horaDeLlegada

    @horaDeLlegada.setter
    def horaDeLlegada(self, horaDeLlegada: str):
        self._horaDeLlegada = horaDeLlegada
    
    @property
    def horaDeSalida(self):
        horaDeSalida = self._horaDeSalida
        return horaDeSalida

    @horaDeSalida.setter
    def horaDeSalida(self, horaDeSalida: str):
        self._horaDeSalida = horaDeSalida

    @property
    def resumenDelDia(self):
        return f"{self.nombre} {self.apellido} llego a las {self.horaDeLlegada} y salio a las {self.horaDeSalida}"
