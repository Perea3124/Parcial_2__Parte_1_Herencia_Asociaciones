from typing import List, Tuple, Optional
from modelo.cliente import Cliente
from modelo.factura import Factura

# Almacenamiento simple en memoria para la demo
CLIENTES: List[Cliente] = []
FACTURAS: List[Factura] = []

def crear_cliente(nombre: str, cedula: str) -> Cliente:
    # evita duplicados por cédula: si existe, devuelve existente
    for c in CLIENTES:
        if c.cedula == cedula:
            return c
    c = Cliente(nombre=nombre, cedula=cedula)
    CLIENTES.append(c)
    return c

def agregar_factura(cliente: Cliente, factura: Factura) -> None:
    # añade factura al cliente y al registro global
    if not hasattr(cliente, "facturas"):
        cliente.facturas = []
    cliente.facturas.append(factura)
    FACTURAS.append(factura)

def buscar_por_cedula(cedula: str) -> Tuple[Optional[Cliente], List[Factura]]:
    """
    Retorna (cliente, lista_de_facturas) si existe, o (None, []) si no.
    """
    for c in CLIENTES:
        if c.cedula == cedula:
            return c, getattr(c, "facturas", [])
    return None, []
