import unittest
from datetime import date
from modelo.producto_control import ProductoControl
from modelo.control_plagas import ControlPlagas
from modelo.fertilizante import Fertilizante

class TestProductosControl(unittest.TestCase):
    def test_crear_producto_control_valido(self):
        p = ProductoControl(nombre="FungicidaX", precio=150.0, codigo_ica="ICA123", frecuencia_aplicacion_dias=14)
        self.assertEqual(p.nombre, "FungicidaX")
        self.assertEqual(p.codigo_ica, "ICA123")
        self.assertEqual(p.frecuencia_aplicacion_dias, 14)

    def test_producto_control_nombre_vacio(self):
        with self.assertRaises(ValueError):
            ProductoControl(nombre="   ", precio=10.0, codigo_ica="ICA1", frecuencia_aplicacion_dias=7)

    def test_control_plagas_periodo_carencia(self):
        c = ControlPlagas(nombre="Insecticida", precio=200.0, codigo_ica="ICA2", frecuencia_aplicacion_dias=30, periodo_carencia_dias=7)
        self.assertEqual(c.periodo_carencia_dias, 7)

    def test_fertilizante_fecha(self):
        f = Fertilizante(nombre="FertA", precio=99.9, codigo_ica="ICA9", frecuencia_aplicacion_dias=60, fecha_ultima_aplicacion=date(2025,1,1))
        self.assertEqual(f.fecha_ultima_aplicacion, date(2025,1,1))

    def test_fertilizante_fecha_invalida(self):
        with self.assertRaises(ValueError):
            Fertilizante(nombre="FertA", precio=99.9, codigo_ica="ICA9", frecuencia_aplicacion_dias=60, fecha_ultima_aplicacion="2025-01-01")

if __name__ == "__main__":
    unittest.main()
