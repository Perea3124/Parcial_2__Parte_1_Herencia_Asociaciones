from dataclasses import dataclass
from typing import Any

@dataclass
class LineaFactura:
    """
    Representa una línea de factura: un producto y una cantidad.
    El 'producto' debe tener al menos el atributo 'precio'.
    """
    producto: Any
    cantidad: int = 1

    def __post_init__(self):
        if not hasattr(self.producto, "precio"):
            raise ValueError("El producto debe tener atributo 'precio'.")
        if not isinstance(self.cantidad, (int, float)) or self.cantidad <= 0:
            raise ValueError("La cantidad debe ser numérica y mayor que 0.")
