from abc import ABC


class Persona(ABC):

    _contador_id = 0 # ID Global

    def __init__(self, nombre: str, apellido: str, telefono: str, correo: str):
        # Generar ID automáticamente
        Persona._contador_id += 1
        self.__id = Persona._contador_id

        # Usar setters
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nombre

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, apellido: str):
        if not apellido:
            raise ValueError("El apellido no puede estar vacío")
        self._apellido = apellido

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, telefono: str):
        if not telefono:
            raise ValueError("El teléfono no puede estar vacío")
        self._telefono = telefono

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, correo: str):
        if not correo:
            raise ValueError("El correo no puede estar vacío")
        self._correo = correo

    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    @property
    def informacion_contacto(self) -> str:
        return f"{self.telefono} - {self.correo}"