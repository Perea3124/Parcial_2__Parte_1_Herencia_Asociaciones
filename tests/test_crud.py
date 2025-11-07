import unittest
from datetime import date
from crud.operaciones import crear_cliente, agregar_factura, buscar_por_cedula, CLIENTES, FACTURAS
from modelo.producto import Producto
from modelo.linea_factura import LineaFactura
from modelo.factura import Factura

class TestCRUDOperaciones(unittest.TestCase):
    def setUp(self):
        # limpiar estados globales entre pruebas
        CLIENTES.clear()
        FACTURAS.clear()

    def test_buscar_por_cedula_no_existe(self):
        cliente, facturas = buscar_por_cedula("0000")
        self.assertIsNone(cliente)
        self.assertEqual(facturas, [])

    def test_crear_cliente_y_factura_y_buscar(self):
        c = crear_cliente("Ana", "111")
        p = Producto(nombre="FertX", precio=50.0)
        lf = LineaFactura(producto=p, cantidad=3)

        # Opción A: crear factura pasando la lista correcta en 'productos'
        f = Factura(fecha=date.today(), productos=[lf])

        # Alternativa (equivalente): crear factura vacía y usar agregar_producto
        # f = Factura(fecha=date.today())
        # f.agregar_producto(lf)

        agregar_factura(c, f)
        cliente, facturas = buscar_por_cedula("111")
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.cedula, "111")
        self.assertEqual(len(facturas), 1)
        # comprobación del total (50 * 3)
        self.assertAlmostEqual(facturas[0].valor_total(), 150.0)

if __name__ == "__main__":
    unittest.main()
