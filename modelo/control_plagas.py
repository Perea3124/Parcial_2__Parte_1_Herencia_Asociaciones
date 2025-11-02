from dataclasses import dataclass
from .producto_control import ProductoControl

@dataclass
class ControlPlagas(ProductoControl):
    """Control de plagas con periodo de carencia (días)."""
    periodo_carencia_dias: int

    def __post_init__(self):
        super().__post_init__()
        if not isinstance(self.periodo_carencia_dias, int) or self.periodo_carencia_dias < 0:
            raise ValueError("periodo_carencia_dias debe ser un entero >= 0.")
