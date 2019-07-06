from sys import maxsize
from os import write
class Ascensor():
    def __init__ (self, tServicios):
        self.estado = True
        self.servicios = []
        self.tServicios = tServicios
        self.tFinal = 0

    def iniciaServicio(self, tInicio):
        duracion = self.tServicios.pop(0)
        self.estado = False
        self.tInicio = tInicio
        self.tFinal = tInicio + duracion 

    def terminaServicio(self):
        self.estado = True
        servicio = (self.tInicio, self.tFinal)
        self.servicios.append(servicio)
        
    def obtenerEstado(self):
        return self.estado

    def __str__(self):
        return "inicio {} termino {}".format( self.tInicio, self.tFinal)