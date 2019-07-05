from sys import maxsize
class Ascensor():
    def __init__ (self):
        self.estado = True
        self.tServicios = []
        self.tFinal = maxsize

    def iniciaServicio(self, tInicio, duracion):
        self.estado = False
        self.tInicio = tInicio
        self.tFinal = tInicio + duracion 

    def terminaServicio(self):
        self.estado = True
        tServicio = (self.tInicio, self.tFinal)
        self.tServicios.append(tServicio)
        self.tFinal = maxsize
        return tServicio[1]
        
    def obtenerEstado(self):
        return self.estado
