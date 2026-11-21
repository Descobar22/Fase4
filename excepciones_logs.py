import logging
from pathlib import Path

class SoftwareFJError(Exception):
    """Excepción base de la aplicación."""

class DatoInvalidoError(SoftwareFJError):
    """Se lanza cuando un campo o parámetro no cumple las reglas de validación."""

class OperacionNoPermitidaError(SoftwareFJError):
    """Se lanza cuando se intenta una transición de estado o acción inválida."""

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un servicio no está habilitado o no tiene capacidad."""

class CalculoInconsistenteError(SoftwareFJError):
    """Se lanza cuando ocurre un error o inconsistencia al calcular costos."""

class ReservaError(SoftwareFJError):
    """Se lanza cuando falla el procesamiento, confirmación o cancelación de una reserva."""

def configurar_logger(
    nombre: str = "SoftwareFJ",
    archivo_log: str = "software_fj.log",
) -> logging.Logger:
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        ruta_log = Path(__file__).resolve().parent / archivo_log
        file_handler = logging.FileHandler(ruta_log, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formato = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        file_handler.setFormatter(formato)
        console_handler.setFormatter(formato)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = configurar_logger()