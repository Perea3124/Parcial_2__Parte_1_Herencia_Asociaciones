from dataclasses import dataclass

@dataclass
class Producto:
    """Clase base simple para productos."""
    nombre: str
    precio: float

    def __post_init__(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not isinstance(self.precio, (int, float)) or self.precio < 0:
            raise ValueError("El precio debe ser un número >= 0.")
