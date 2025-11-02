import unittest
from datetime import date, timedelta
from modelo.factura import Factura
from modelo.cliente import Cliente
from modelo.producto import Producto
from modelo.fertilizante import Fertilizante
from modelo.producto_control import ProductoControl
from modelo.linea_factura import LineaFactura

class DummyConCantidad(Producto):
    def __init__(self, nombre, precio, cantidad=1):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class TestFacturaCliente(unittest.TestCase):
    def test_valor_total_simple(self):
        p1 = DummyConCantidad("Item1", 10.0)
        p2 = DummyConCantidad("Item2", 5.5, cantidad=2)
        f = Factura(fecha=date.today(), productos=[p1, p2])
        self.assertAlmostEqual(f.valor_total(), 10.0 + 5.5*2)

    def test_agregar_producto(self):
        f = Factura(fecha=date.today())
        p = DummyConCantidad("X", 7.0, cantidad=3)
        f.agregar_producto(p)
        self.assertEqual(len(f.productos), 1)
        self.assertAlmostEqual(f.valor_total(), 7.0*3)

    def test_cliente_total_y_facturas_desde(self):
        c = Cliente(nombre="Juan", cedula="12345")
        f1 = Factura(fecha=date.today() - timedelta(days=10), productos=[DummyConCantidad("A", 10)])
        f2 = Factura(fecha=date.today() - timedelta(days=2), productos=[DummyConCantidad("B", 20)])
        c.agregar_factura(f1)
        c.agregar_factura(f2)
        self.assertAlmostEqual(c.total_facturado(), 30.0)
        rec = c.facturas_desde(date.today() - timedelta(days=5))
        self.assertEqual(len(rec), 1)
        self.assertEqual(rec[0].fecha, f2.fecha)

    def test_factura_rechaza_producto_sin_precio(self):
        class BadProd:
            pass
        f = Factura(fecha=date.today())
        with self.assertRaises(ValueError):
            f.agregar_producto(BadProd())

    def test_valor_total_con_linea_factura(self):
        fert = Fertilizante(nombre="FertA", precio=50.0, codigo_ica="ICA1", frecuencia_aplicacion_dias=30)
        linea = LineaFactura(producto=fert, cantidad=3)
        f = Factura(fecha=date.today(), productos=[linea])
        self.assertAlmostEqual(f.valor_total(), 150.0)

if __name__ == "__main__":
    unittest.main()
