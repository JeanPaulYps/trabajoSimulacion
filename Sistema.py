from Ascensor import Ascensor
from Persona import Persona

class Sistema():
    def __init__ (self, ascensor1, ascensor2, tLlegadas):
        self.personasEnCola = []
        self.personas = []
        self.relojSimulacion = []
        self.ascensor1 = ascensor1
        self.ascensor2 = ascensor2
        self.tLlegadas = tLlegadas

    def personaSubeAscensor(self, ascensor):
        persona = Persona(self.tLlegadas.pop())
        self.personas.append(persona)
        ascensor.iniciaServicio(persona.tLlegada())

    def personasEnColaSubenAlAscensor(self, ascensor):
        ascensor.terminaServicio()
        ascensor.iniciaServicio(ascensor.tFinal)
        del(self.personasEnCola[0:8])


    def personaEntraALaCola(self):
        persona = Persona(self.tLlegadas.pop())
        self.personas.append(persona)
        self.personasEnCola.append(persona)

    

    def relizarSimulacion(self):
        self.personaSubeAscensor(self.ascensor1)
        while(self.tLlegadas):
            #Condicional V1
            if (not self.personasEnCola):
                if (self.ascensor1.estado):
                    self.personaSubeAscensor(self.ascensor1)
                elif (self.ascensor2.estado):
                    self.personaSubeAscensor(self.ascensor2)
                elif (self.ascensor1.tFinal < self.ascensor2.tfina):
                    self.ascensor1.terminaServicio()
                elif (self.ascensor2.tFinal < self.ascensor1.tfinal):
                    self.ascensor2.terminaServicio()
            else:
                if (self.tLlegadas[-1] < self.ascensor1.tFinal < self.ascensor2.tFinal):
                    self.personaEntraALaCola()
                elif (self.ascensor1.tFinal < self.ascensor2.tfinal < self.tLlegadas[-1]):
                    self.personasEnColaSubenAlAscensor(self.ascensor1)
                elif (self.ascensor2.tFinal < self.ascensor1.tfinal < self.tLlegadas[-1]):
                    self.personasEnColaSubenAlAscensor(self.ascensor2)

            ##Condicional V2
            if (self.ascensor1.estado and not self.personasEnCola):
                self.personaSubeAscensor(self.ascensor1)
            elif (self.ascensor2.estado and not self.personasEnCola):
                self.personaSubeAscensor(self.ascensor2)
            elif (self.tLlegadas[-1] < self.ascensor1.tFinal < self.ascensor2.tFinal and self.personasEnCola):
                self.personaEntraALaCola()
            elif (self.ascensor1.tFinal < self.ascensor2.tfinal < self.tLlegadas[-1] and self.personasEnCola):
                self.personasEnColaSubenAlAscensor(self.ascensor1)
            elif (self.ascensor2.tFinal < self.ascensor1.tfinal < self.tLlegadas[-1] and self.personasEnCola):
                self.personasEnColaSubenAlAscensor(self.ascensor2)
            else:
                if (self.ascensor1.tFinal < self.ascensor2.tfina):
                    self.ascensor1.terminaServicio()
                elif (self.ascensor2.tFinal < self.ascensor1.tfinal):
                    self.ascensor2.terminaServicio()