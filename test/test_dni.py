import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../dni')))

from dni import DNI

class TestDNI(unittest.TestCase):
    def test_dni_valido(self):
        un_dni = DNI("23000000T")
        self.assertTrue(un_dni.valido)
        self.assertEqual(un_dni.numero, 23000000)
        self.assertEqual(un_dni.letra, "T")
        self.assertEqual(un_dni.confianza, 1)

    def test_dni_corregible_con_puntos_y_guion(self):
        un_dni = DNI("23.000.000-T")
        self.assertTrue(un_dni.valido)
        self.assertEqual(un_dni.numero, 23000000)
        self.assertEqual(un_dni.letra, "T")
        self.assertEqual(un_dni.confianza, 0.5)

    def test_dni_con_espacio(self):
        un_dni = DNI("23000000 T")
        self.assertTrue(un_dni.valido)
        self.assertEqual(un_dni.numero, 23000000)
        self.assertEqual(un_dni.letra, "T")
        self.assertEqual(un_dni.confianza, 1)

    def test_dni_corregible_con_puntos_y_espacio(self):
        un_dni = DNI("23.000.000 T")
        self.assertTrue(un_dni.valido)
        self.assertEqual(un_dni.numero, 23000000)
        self.assertEqual(un_dni.letra, "T")
        self.assertEqual(un_dni.confianza, 0.5)

    def test_dni_con_ceros_iniciales(self):
        un_dni = DNI("00023000T")
        self.assertTrue(un_dni.valido)
        self.assertEqual(un_dni.numero, 23000)
        self.assertEqual(un_dni.letra, "T")
        self.assertEqual(un_dni.confianza, 1)

    def test_dni_letra_minuscula(self):
        un_dni = DNI("23000t")
        self.assertTrue(un_dni.valido)
        self.assertEqual(un_dni.numero, 23000)
        self.assertEqual(un_dni.letra, "T")
        self.assertEqual(un_dni.confianza, 1)

    def test_dni_invalido(self):
        un_dni = DNI("1234567A")
        self.assertFalse(un_dni.valido)
        self.assertEqual(un_dni.numero, 1234567)
        self.assertEqual(un_dni.letra, "A")
        self.assertEqual(un_dni.confianza, 0)

    def test_dni_demasiados_digitos(self):
        un_dni = DNI("123456789T")
        self.assertFalse(un_dni.valido)
        self.assertIsNone(un_dni.numero)
        self.assertIsNone(un_dni.letra)
        self.assertEqual(un_dni.confianza, 0)

    def test_dni_corregible_con_puntos_y_guion(self):
        un_dni = DNI(".23.000.000-T")
        self.assertTrue(un_dni.valido)
        self.assertEqual(un_dni.numero, 23000000)
        self.assertEqual(un_dni.letra, "T")
        self.assertEqual(un_dni.confianza, 0.5)

    def test_dni_corregible_con_guiones_y_espacios(self):
        un_dni0 = DNI("23000.000-T")
        self.assertTrue(un_dni0.valido)
        self.assertEqual(un_dni0.numero, 23000000)
        self.assertEqual(un_dni0.letra, "T")
        self.assertEqual(un_dni0.confianza, 0.5)

if __name__ == '__main__':
    unittest.main()
