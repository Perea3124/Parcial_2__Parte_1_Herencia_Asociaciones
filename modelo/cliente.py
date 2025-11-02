from dataclasses import dataclass, field
from typing import List
from datetime import date
from .factura import Factura

@dataclass
class Cliente:
    nombre: str
    cedula: str
    facturas: List[Factura] = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")
        if not isinstance(self.cedula, str) or not self.cedula.strip():
            raise ValueError("La cédula del cliente no puede estar vacía.")
        if not isinstance(self.facturas, list):
            raise ValueError("facturas debe ser una lista de Factura.")

    def agregar_factura(self, factura: Factura) -> None:
        if not isinstance(factura, Factura):
            raise ValueError("Debe agregarse una instancia de Factura.")
        self.facturas.append(factura)

    def total_facturado(self) -> float:
        total = 0.0
        for f in self.facturas:
            total += f.valor_total()
        return total

    def facturas_desde(self, desde: date):
        """Devuelve facturas con fecha >= desde."""
        return [f for f in self.facturas if f.fecha >= desde]
