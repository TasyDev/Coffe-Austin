from abc import ABC

class Producto(ABC):

    _contador_id = 0

    def __init__(self, nombre: str, precio: float, descripcion: str, disponible: bool):

        Producto._contador_id += 1
        self.__id = Producto._contador_id

        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.disponible = disponible

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.nombre

    @property
    def precio(self):
        return self.precio

    @property
    def descripcion(self):
        return self.descripcion

    @property
    def disponible(self):
        return self.disponible

    @disponible.setter
    def disponible(self, disponible: bool):
        self.disponible = disponible
