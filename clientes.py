"""Módulo 2: Entidad base abstracta y gestión encapsulada de Clientes."""

from abc import ABC, abstractmethod
from datetime import datetime
import re

from estudiante1_excepciones_logs import DatoInvalidoError
class EntidadSistema(ABC):
    """Clase abstracta base para todas las entidades del sistema."""

    def __init__(self, id_entidad: str) -> None:
        if not isinstance(id_entidad, str) or not id_entidad.strip():
            raise DatoInvalidoError("El ID de la entidad debe ser un texto no vacío.")
        self._id_entidad: str = id_entidad.strip().upper()
        self._fecha_creacion: datetime = datetime.now()

    @property
    def id_entidad(self) -> str:
        return self._id_entidad

    @property
    def fecha_creacion(self) -> datetime:
        return self._fecha_creacion

    @abstractmethod
    def describir(self) -> str:
        """Retorna una descripción legible de la entidad."""

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} id={self._id_entidad}>"

class Cliente(EntidadSistema):
    """Representa un cliente con datos encapsulados y validación estricta."""

    _REGEX_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(self, id_entidad: str, nombre: str, correo: str, telefono: str) -> None:
        super().__init__(id_entidad)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self._activo: bool = True

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatoInvalidoError("El nombre del cliente debe tener al menos 2 caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        if not isinstance(valor, str) or not self._REGEX_EMAIL.match(valor.strip()):
            raise DatoInvalidoError(f"Correo electrónico inválido: '{valor}'.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        limpio = re.sub(r"[\s\-()]", "", str(valor))
        if not limpio.isdigit() or len(limpio) < 7:
            raise DatoInvalidoError(f"Teléfono inválido: '{valor}'. Debe tener al menos 7 dígitos.")
        self._telefono = limpio

    @property
    def activo(self) -> bool:
        return self._activo

    def desactivar(self) -> None:
        self._activo = False

    def activar(self) -> None:
        self._activo = True

    def describir(self) -> str:
        estado = "Activo" if self._activo else "Inactivo"
        return (
            f"Cliente [{self._id_entidad}] {self._nombre} | "
            f"Correo: {self._correo} | Estado: {estado}"
        )
