from dataclasses import dataclass
from .producto import Producto

@dataclass
class ProductoControl(Producto):
    """Producto sujeto a control (ICA u otro identificador)."""
    codigo_ica: str
    frecuencia_aplicacion_dias: int  # número de días entre aplicaciones

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.codigo_ica, str) or not self.codigo_ica.strip():
            raise ValueError("codigo_ica no puede estar vacío.")
        if not isinstance(self.frecuencia_aplicacion_dias, int) or self.frecuencia_aplicacion_dias <= 0:
            raise ValueError("frecuencia_aplicacion_dias debe ser un entero mayor que 0.")
