from dataclasses import dataclass
from enum import Enum

class TipoAnimal(Enum):
    BOVINO = "bovino"
    CAPRINO = "caprino"
    PORCINO = "porcino"

@dataclass
class Antibiotico:
    """Antibiótico para animales con validación de dosis y tipo de animal."""
    nombre: str
    precio: float
    dosis_mg_por_kg: int  # por ejemplo 400..600
    tipo_animal: TipoAnimal

    def __post_init__(self):
        # nombre
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ValueError("El nombre del antibiótico no puede estar vacío.")
        # precio
        if not isinstance(self.precio, (int, float)) or self.precio < 0:
            raise ValueError("El precio debe ser un número >= 0.")
        # dosis
        if not isinstance(self.dosis_mg_por_kg, int):
            raise ValueError("La dosis debe ser un entero (mg/kg).")
        if not (400 <= self.dosis_mg_por_kg <= 600):
            raise ValueError("La dosis válida está entre 400 y 600 mg/kg.")
        # tipo de animal
        if not isinstance(self.tipo_animal, TipoAnimal):
            raise ValueError("tipo_animal debe ser un miembro de TipoAnimal Enum.")
