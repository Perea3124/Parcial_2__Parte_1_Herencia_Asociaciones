import unittest
from modelo.antibiotico import Antibiotico, TipoAnimal

class TestAntibiotico(unittest.TestCase):
    def test_antibiotico_valido(self):
        a = Antibiotico(nombre="AntibioX", precio=120.0, dosis_mg_por_kg=450, tipo_animal=TipoAnimal.BOVINO)
        self.assertEqual(a.nombre, "AntibioX")
        self.assertEqual(a.dosis_mg_por_kg, 450)
        self.assertEqual(a.tipo_animal, TipoAnimal.BOVINO)

    def test_antibiotico_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Antibiotico(nombre="   ", precio=50.0, dosis_mg_por_kg=500, tipo_animal=TipoAnimal.PORCINO)

    def test_antibiotico_dosis_fuera_rango(self):
        with self.assertRaises(ValueError):
            Antibiotico(nombre="Ant", precio=10.0, dosis_mg_por_kg=200, tipo_animal=TipoAnimal.CAPRINO)

    def test_antibiotico_tipo_invalido(self):
        with self.assertRaises(ValueError):
            # pasar un string en lugar de TipoAnimal debe fallar
            Antibiotico(nombre="Ant", precio=10.0, dosis_mg_por_kg=450, tipo_animal="bovino")

if __name__ == "__main__":
    unittest.main()
