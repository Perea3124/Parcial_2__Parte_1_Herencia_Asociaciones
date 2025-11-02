from dataclasses import dataclass, field
from datetime import date
from typing import Any, List

from .linea_factura import LineaFactura

@dataclass
class Factura:
    """
    Factura que acepta elementos de tipo:
      - LineaFactura(producto, cantidad)
      - objetos producto con atributo 'cantidad' (opcional)
      - objetos producto simples (se asume cantidad = 1)
    """
    fecha: date
    productos: List[Any] = field(default_factory=list)

    def __post_init__(self):
        if not isinstance(self.fecha, date):
            raise ValueError("fecha debe ser datetime.date")
        if not isinstance(self.productos, list):
            raise ValueError("productos debe ser una lista")

    def valor_total(self) -> float:
        total = 0.0
        for item in self.productos:
            if isinstance(item, LineaFactura):
                prod = item.producto
                cantidad = item.cantidad
            else:
                prod = item
                cantidad = getattr(prod, "cantidad", 1)
            # validaciones sobre el producto
            if not hasattr(prod, "precio"):
                raise ValueError("Cada producto debe tener atributo 'precio'")
            precio = getattr(prod, "precio")
            if not isinstance(precio, (int, float)):
                raise ValueError("El precio del producto debe ser numérico")
            if not isinstance(cantidad, (int, float)):
                raise ValueError("La cantidad debe ser numérica")
            total += precio * cantidad
        return total

    def agregar_producto(self, producto: Any) -> None:
        """
        Añade una LineaFactura o un producto (con o sin atributo 'cantidad').
        Si se pasa un objeto sin 'precio' -> ValueError.
        """
        if isinstance(producto, LineaFactura):
            # ya validado en LineaFactura.__post_init__
            self.productos.append(producto)
            return
        # si es un objeto producto simple, verificar precio
        if not hasattr(producto, "precio"):
            raise ValueError("El producto debe tener atributo 'precio'")
        self.productos.append(producto)
