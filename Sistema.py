from Ascensor import Ascensor
from Persona import Persona

class Sistema():
    EVENTOS = {"Persona": "Llega Persona", "AscensorTermina": "Ascensor {} Termina", 
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
        tiempo = self.tLlegadas.pop(0)
        persona = Persona(tiempo)
        self.personas.append(persona)
        self.personasEnCola.append(persona)

        self.relojSimulacion.append(tiempo)
        self.resultadosSimulacion.append((tiempo, self.EVENTOS["PersonaCola"], str(persona)))

    def llegaAscensor1(self):
        return (min(self.tLlegadas[0], self.ascensor1.tFinal, self.ascensor2.tFinal)  == self.ascensor1.tFinal) and not self.ascensor1.estado
    
    def llegaAscensor2(self):
        return min(self.tLlegadas[0], self.ascensor2.tFinal) == self.ascensor1.tFinal and not self.ascensor2.estado

    def ascensor1LlegaPrimero(self):
        return self.ascensor1.tFinal < self.ascensor2.tFinal 

    def ascensor2LlegaPrimero(self):
        return self.ascensor2.tFinal < self.ascensor1.tFinal 

    def ascensorTerminaServicio(self, ascensor, numero):
        tiempo = ascensor.tFinal
        ascensor.terminaServicio()
        self.resultadosSimulacion.append( (tiempo, self.EVENTOS["AscensorTermina"].format(numero)
                                        , str(ascensor)))
        
    def relizarSimulacion(self):
        self.personaSubeAscensor(self.ascensor1)
        while(self.tLlegadas or self.personasEnCola 
            or not self.ascensor1.estado or not self.ascensor2.estado):
            if self.tLlegadas:
                if self.llegaAscensor1():
                    self.ascensorTerminaServicio(self.ascensor1,1)
                elif self.llegaAscensor2():
                    self.ascensorTerminaServicio(self.ascensor2,2)
                else:
                    if not self.personasEnCola:
                        if self.ascensor1.estado:
                            self.personaSubeAscensor(self.ascensor1)
                        elif self.ascensor2.estado:
                            self.personaSubeAscensor(self.ascensor2)
                        else:
                            self.personaEntraALaCola()
                    else:
                        if self.ascensor1.estado:
                            self.personasEnColaSubenAlAscensor(self.ascensor1)
                        elif self.ascensor2.estado:
                            self.personasEnColaSubenAlAscensor(self.ascensor2)
                        else:
                            self.personaEntraALaCola()

            elif self.personasEnCola:
                if self.ascensor1.estado:
                    self.personasEnColaSubenAlAscensor(self.ascensor1)
                elif self.ascensor2.estado:
                    self.personasEnColaSubenAlAscensor(self.ascensor2)
                else:
                    if self.ascensor1LlegaPrimero():
                        self.ascensorTerminaServicio(self.ascensor1,1)
                    else:
                        self.ascensorTerminaServicio(self.ascensor2,2)
            
            else:
                if self.ascensor1LlegaPrimero():
                    self.ascensorTerminaServicio(self.ascensor1,1)
                elif self.ascensor2LlegaPrimero():
                    self.ascensorTerminaServicio(self.ascensor2,2)
                elif not self.ascensor1.estado:
                    self.ascensorTerminaServicio(self.ascensor1,1)
                else:
                    self.ascensorTerminaServicio(self.ascensor2,2)



    def escribirResultados (self):
        archivo = open("resultados.txt", "w+")
        for resultado in self.resultadosSimulacion:
            archivo.write( "{}\t\t\t\t{}\t\t\t\t{}\n".format(resultado[0], resultado[1],
                            resultado[2]))
        archivo.close()