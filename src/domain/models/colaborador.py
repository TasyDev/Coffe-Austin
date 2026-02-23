from datetime import datetime
from .persona import Persona

class Colaborador(Persona):
    def __init__(self, nombre: str, apellido: str, telefono: str, correo: str, fechaDeIngreso: datetime, salario: int, cargo: str):
        super().__init__(nombre, apellido, telefono, correo)
        self._fechaDeIngreso = fechaDeIngreso
        self._salario = salario
        self._cargo = cargo    
    
    @property
    def fechaDeIngreso(self):
        fechaDeIngreso = self._fechaDeIngreso
        return fechaDeIngreso

    @fechaDeIngreso.setter
    def fechaDeIngreso(self, fechaDeIngreso: datetime):
        self._fechaDeIngreso = fechaDeIngreso
    
    @property   
    def salario(self):
        salario = self._salario
        return salario

    @salario.setter
    def salario(self, salario: int):
        self._salario = salario
    
    @property
    def cargo(self):
        cargo = self._cargo
        return cargo

    @cargo.setter
    def cargo(self, cargo: str):
        self._cargo = cargo