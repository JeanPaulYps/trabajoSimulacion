class Ascensor():
    def __init__ (self):
        self.estado = True
        self.tServicios = []
        self.tInicio = 0
        self.tFinal = 0

    def iniciaServicio(self, tInicio, duracion):
        self.estado = False
        self.tInicio = tInicio
        self.tFinal = tInicio + duracion 

    def terminaServicio(self):
        self.estado = True
        tServicio = (self.tInicio, self.tFinal)
        self.tServicios.append(tServicio)
        
    def obtenerEstado(self):
        return self.estado
