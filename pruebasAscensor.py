import unittest
from Ascensor import Ascensor
from sys import maxsize

class PruebasPersona(unittest.TestCase):

    def test_iniciaServicio(self):
        ascensor = Ascensor()
        ascensor.iniciaServicio(20,10)
        self.assertFalse(ascensor.estado)
        self.assertEqual(ascensor.tInicio, 20)
        self.assertEqual(ascensor.tFinal, 30)
        self.assertEqual(ascensor.terminaServicio(), 30)
        self.assertTrue(ascensor.estado)
        self.assertEqual(ascensor.tServicios, [(20,30)])
        self.assertEqual(ascensor.tFinal, maxsize)

    def test_servicios(self):
        ascensor = Ascensor()
        ascensor.iniciaServicio(20,10)
        ascensor.terminaServicio()
        ascensor.iniciaServicio(40, 20)
        ascensor.terminaServicio()
        self.assertEqual(ascensor.tServicios, [(20,30), (40,60)])

if __name__ == "__main__":
    unittest.main()