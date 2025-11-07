from datetime import date
from crud.operaciones import crear_cliente, agregar_factura, buscar_por_cedula
from modelo.producto import Producto
from modelo.linea_factura import LineaFactura
from modelo.factura import Factura

def demo_crear_y_buscar():
    """
    Demo mínimo: crear un cliente, añadir una factura con una LineaFactura,
    luego buscar por cédula e imprimir información para verificar en la consola
    y en el depurador.
    """
    # Crear cliente
    cliente = crear_cliente("Cliente Demo", "99999")

    # Crear producto y linea
    producto = Producto(nombre="DemoProducto", precio=42.5)
    linea = LineaFactura(producto=producto, cantidad=2)

    # Crear factura (usar campo 'productos' según la implementación)
    factura = Factura(fecha=date.today(), productos=[linea])

    # Agregar factura al cliente
    agregar_factura(cliente, factura)

    # Buscar por cédula
    encontrado, facturas = buscar_por_cedula("99999")

    # Salidas para validar por consola y por debug
    print("Cliente encontrado:", encontrado.nombre if encontrado else None)
    print("Número de facturas:", len(facturas))
    for f in facturas:
        print("Fecha:", f.fecha, "Total:", f.valor_total())

    # Punto práctico para breakpoint en depuración:
    # deja la variable 'encontrado' y 'facturas' en el scope
    return encontrado, facturas

if __name__ == "__main__":
    demo_crear_y_buscar()
