import Ascensor, Persona 
class Sistema():
    def __init__ (self, ascensor1, ascensor2, tLlegadas):
        self.personasEnCola = []
        self.personas = []
        self.relojSimulacion = []
        self.ascensor1 = ascensor1
        self.ascensor2 = ascensor2
        self.tLlegadas = tLlegadas

    def personaSubeAscensor(ascensor):
        persona = Persona(self.tLlegadas.pop())
        self.personas.append(persona)
        ascensor.iniciaServicio(persona.tLlegada())

    def personasEnColaSubenAlAscensor(ascensor):
        ascensor.terminaServicio()
        ascensor.iniciaServicio(ascensor.tFinal)
        del(self.personasEnCola[0:8])


    def personaEntraALaCola(self):
        persona = Persona(tLlegadas.pop())
        self.personas.append(persona)
        self.personasEnCola.append(persona)

    def relizarSimulacion(self):
        personaSubeAscensor(ascensor1)
        while(self.tLlegadas):
            #Condicional V1
            if (not self.personasEnCola):
                if (self.ascensor1.estado):
                    personaSubeAscensor(ascensor1)
                elif (self.ascensor2.estado):
                    personaSubeAscensor(ascensor2)
                elif (ascensor1.tFinal < ascensor2.tfina):
                    ascensor1.terminaServicio()
                elif (ascensor2.tFinal < ascensor1.tfinal):
                    ascensor2.terminaServicio()
            else:
                if (tLlegadas[-1] < ascensor1.tFinal < ascensor2.tFinal):
                    personaEntraALaCola()
                elif (ascensor1.tFinal < ascensor2.tfinal < tLlegadas[-1]):
                    personasEnColaSubenAlAscensor(ascensor1)
                elif (ascensor2.tFinal < ascensor1.tfinal < tLlegadas[-1]):
                    personasEnColaSubenAlAscensor(ascensor2)

            ##Condicional V2
            if (self.ascensor1.estado and not self.personasEnCola):
                personaSubeAscensor(ascensor1)
            elif (self.ascensor2.estado and not self.personasEnCola):
                personaSubeAscensor(ascensor2)
            elif (tLlegadas[-1] < ascensor1.tFinal < ascensor2.tFinal and self.personasEnCola):
                personaEntraALaCola()
            elif (ascensor1.tFinal < ascensor2.tfinal < tLlegadas[-1] and self.personasEnCola):
                personasEnColaSubenAlAscensor(ascensor1)
            elif (ascensor2.tFinal < ascensor1.tfinal < tLlegadas[-1] and self.personasEnCola):
                personasEnColaSubenAlAscensor(ascensor2)
            else:
                if (ascensor1.tFinal < ascensor2.tfina):
                    ascensor1.terminaServicio()
                elif (ascensor2.tFinal < ascensor1.tfinal):
                    ascensor2.terminaServicio()