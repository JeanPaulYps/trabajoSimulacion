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
            """
            Verificar que accion ocurre primero: 
                -Llega persona
                -Llega ascensor 1
                -Llega ascensor 2
            Verificar si hay cola:
                -Hay cola
                -No hay cola
            Hacer un producto cartesiano de hay cola o no hay cola:
                -Llega persona hay cola => forma en cola
                -Llega ascensor 1 hay cola => termina servicio y sube gente al ascensor
                -Llega ascensor 2 hay cola => termina servicio y sube gente al ascensor
                -Llega persona no hay cola => toma ascensor 
                -Llega ascensor 1 no hay cola => termina servicio 
                -Llega ascensor 2 no hay cola => termina servicio 
            """
            if (self.tLlegadas[-1] < self.ascensor1.tFinal < self.ascensor2.tFinal):
                if (not self.personasEnCola):
                    if (self.ascensor1.estado):
                        self.personaSubeAscensor(self.ascensor1)
                    elif (self.ascensor2.estado):
                        self.personaSubeAscensor(self.ascensor2)
                else:
                    self.personaEntraALaCola()
                    
            elif (self.ascensor1.tFinal < self.ascensor2.tfinal < self.tLlegadas[-1]):
                if (not self.personasEnCola):
                    self.ascensor1.terminaServicio()
                elif (self.personasEnCola):
                    self.personasEnColaSubenAlAscensor(self.ascensor1)

                """elif (self.ascensor1.tFinal < self.ascensor2.tfina):
                    self.ascensor1.terminaServicio()
                elif (self.ascensor2.tFinal < self.ascensor1.tfinal):
                    self.ascensor2.terminaServicio()"""
            """else:
                if (self.tLlegadas[-1] < self.ascensor1.tFinal < self.ascensor2.tFinal):
                    self.personaEntraALaCola()
                elif (self.ascensor1.tFinal < self.ascensor2.tfinal < self.tLlegadas[-1]):
                    self.personasEnColaSubenAlAscensor(self.ascensor1)
                elif (self.ascensor2.tFinal < self.ascensor1.tfinal < self.tLlegadas[-1]):
                    self.personasEnColaSubenAlAscensor(self.ascensor2)"""