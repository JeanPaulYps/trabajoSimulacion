from Ascensor import Ascensor
from Persona import Persona

class Sistema():
    EVENTOS = {"Persona": "Llega Persona", "AscensorTermina": "Ascensor Termina", 
                "ColaSube": "Personas suben ascensor", "PersonaSube": "Persona sube ascensor",
                "PersonaCola": "Persona entra a la cola"}
    def __init__ (self, ascensor1, ascensor2, tLlegadas):
        self.personasEnCola = []
        self.personas = []
        self.relojSimulacion = []
        self.resultadosSimulacion = [("Tiempo", "Evento", "Cambios de estados") ]
        self.ascensor1 = ascensor1
        self.ascensor2 = ascensor2
        self.tLlegadas = tLlegadas

    def personaSubeAscensor(self, ascensor):
        tiempo = self.tLlegadas.pop(0)
        persona = Persona(tiempo)
        self.personas.append(persona)
        ascensor.iniciaServicio(persona.tLlegada) 
        persona.asignartServicio(persona.tLlegada)

        self.relojSimulacion.append(tiempo)
        self.resultadosSimulacion.append( (tiempo, self.EVENTOS["PersonaSube"], str(persona)) ) 

    def asignarTiemposDeServicio (self, tServicio):
        for persona in self.personasEnCola[0:8]:
            persona.asignartServicio(tServicio)

    def personasEnColaSubenAlAscensor(self, ascensor):
        tiempo = ascensor.tFinal
        ascensor.iniciaServicio(tiempo)
        self.asignarTiemposDeServicio(tiempo)
        del(self.personasEnCola[0:8])

        self.relojSimulacion.append(tiempo)
        self.resultadosSimulacion.append( (tiempo, self.EVENTOS["ColaSube"], str(ascensor)) )

    def personaEntraALaCola(self):
        tiempo = self.tLlegadas.pop()
        persona = Persona(tiempo)
        self.personas.append(persona)
        self.personasEnCola.append(persona)

        self.relojSimulacion.append(tiempo)
        self.resultadosSimulacion.append((tiempo, self.EVENTOS["PersonaCola"], str(persona)))

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
            Verificar si hay ascensor:
                -Hay ascensor
                -No hay ascensor
            Hacer un producto cartesiano de hay cola o no hay cola:
                -Llega persona hay cola => forma en cola
                -Llega ascensor 1 hay cola => termina servicio y sube gente al ascensor
                -Llega ascensor 2 hay cola => termina servicio y sube gente al ascensor
                -Llega persona no hay cola => toma ascensor 
                -Llega ascensor 1 no hay cola => termina servicio 
                -Llega ascensor 2 no hay cola => termina servicio 
            """
            if self.ascensor1.estado or self.ascensor2.estado:
                if not self.personasEnCola:
                    if self.ascensor1.estado:
                        self.personaSubeAscensor(self.ascensor1)
                    else:
                        self.personaSubeAscensor(self.ascensor2)
                else:
                    if self.ascensor1.estado:
                        self.personasEnColaSubenAlAscensor(self.ascensor1)
                    else:
                        self.personasEnColaSubenAlAscensor(self.ascensor2)
            else:
                if (min(self.tLlegadas[-1], self.ascensor1.tFinal, self.ascensor2.tFinal) 
                    == self.tLlegadas[-1] ):
                    self.personaEntraALaCola()          
                elif (min(self.tLlegadas[-1], self.ascensor1.tFinal, self.ascensor2.tFinal)
                    == self.ascensor1.tFinal ):
                    tiempo = self.ascensor1.tFinal
                    self.ascensor1.terminaServicio()
                    self.resultadosSimulacion.append( (tiempo, self.EVENTOS["AscensorTermina"], str(self.ascensor1)) )

                elif (min(self.tLlegadas[-1], self.ascensor1.tFinal, self.ascensor2.tFinal) 
                    == self.ascensor2.tFinal ):
                    tiempo = self.ascensor2.tFinal
                    self.ascensor2.terminaServicio()
                    self.resultadosSimulacion.append( (tiempo, self.EVENTOS["AscensorTermina"], str(self.ascensor2)) )

        if  not self.ascensor1.estado:
            tiempo = self.ascensor1.tFinal
            self.ascensor1.terminaServicio()
            self.resultadosSimulacion.append( (tiempo, self.EVENTOS["AscensorTermina"], str(self.ascensor1)) )
        if  not self.ascensor2.estado:
            tiempo = self.ascensor2.tFinal
            self.ascensor2.terminaServicio()
            self.resultadosSimulacion.append( (tiempo, self.EVENTOS["AscensorTermina"], str(self.ascensor2)) )