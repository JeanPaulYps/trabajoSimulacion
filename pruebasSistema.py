import unittest
from Ascensor import Ascensor
from Persona import Persona
from Sistema import Sistema
from sys import maxsize

class PruebasSistema(unittest.TestCase):
    def test_crearSistema(self):
        ascensor1 = Ascensor([10,10,10])
        ascensor2 = Ascensor([10,10,10])
        tLlegadas = [5,20,30]
        sistema = Sistema(ascensor1,ascensor2,tLlegadas)
        self.assertEqual(sistema.ascensor1, ascensor1)
        self.assertEqual(sistema.ascensor2, ascensor2)
        self.assertEqual(sistema.tLlegadas, [5,20,30])

    def test_personaSubeAscensor (self):
        ascensor1 = Ascensor([10,10,10])
        ascensor2 = Ascensor([10,10,10])
        tLlegadas = [5,20,30]
        sistema = Sistema(ascensor1,ascensor2,tLlegadas)
        sistema.personaSubeAscensor(ascensor1)
        self.assertEqual(sistema.tLlegadas, [20,30])
        self.assertFalse(ascensor1.estado)
        self.assertEqual(len(sistema.personas), 1)
        self.assertEqual(sistema.personas[0].tLlegada, 5)
        self.assertEqual(ascensor1.tFinal, 15)

    def test_realizarSimulacion (self):
        ascensor1 = Ascensor([10])
        ascensor2 = Ascensor([10])
        tLlegadas = [5]
        sistema = Sistema(ascensor1,ascensor2,tLlegadas)
        sistema.relizarSimulacion()
        self.assertEqual(sistema.tLlegadas, [])
        self.assertTrue(ascensor1.estado)
        self.assertEqual(len(sistema.personas), 1)
        self.assertEqual(sistema.personas[0].tLlegada, 5)
        self.assertEqual(ascensor1.tFinal, 15)
        sistema.escribirResultados()        

if __name__ == "__main__":
    unittest.main()