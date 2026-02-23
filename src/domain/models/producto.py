from abc import ABC

class Producto(ABC):

    _contador_id = 0

    def __init__(self, nombre: str, precio: float, descripcion: str, disponible: bool):

        Producto._contador_id += 1
        self.__id = Producto._contador_id

        self._nombre = nombre
        self._precio = precio
        self._descripcion = descripcion
        self._disponible = disponible

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, disponible: bool):
        self._disponible = disponible
