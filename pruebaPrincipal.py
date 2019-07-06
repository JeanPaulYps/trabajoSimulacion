import unittest
from Ascensor import Ascensor
from Persona import Persona
from Sistema import Sistema

class PruebaPrincipal (unittest.TestCase):

    def setUp(self):
        self.ascensor1 = Ascensor([20,15, 20])
        self.ascensor2 = Ascensor([20,10])
        self.tLlegadas = [0,5,7.5,9,11,13,16,19,30, 45]
        self.sistema = Sistema(self.ascensor1,self.ascensor2,self.tLlegadas)
        

    def test(self):
            self.sistema.relizarSimulacion()
            self.sistema.escribirResultados()
            self.assertEqual(len(self.sistema.resultadosSimulacion), 15)
            self.assertEqual(self.sistema.tLlegadas, [])
            self.assertEqual(self.ascensor1.tServicios, [])
            print(self.ascensor1.estado)

    def tearDown(self):
        del(self.sistema)

if __name__ == '__main__':
    unittest.main() 