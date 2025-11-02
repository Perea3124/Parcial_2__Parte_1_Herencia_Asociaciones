from dataclasses import dataclass
from datetime import date
from .producto_control import ProductoControl

@dataclass
class Fertilizante(ProductoControl):
    """Fertilizante con fecha de última aplicación (opcional)."""
    fecha_ultima_aplicacion: date | None = None

    def __post_init__(self):
        super().__post_init__()
        if self.fecha_ultima_aplicacion is not None and not isinstance(self.fecha_ultima_aplicacion, date):
            raise ValueError("fecha_ultima_aplicacion debe ser datetime.date o None.")
