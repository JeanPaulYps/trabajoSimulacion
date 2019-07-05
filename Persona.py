class Persona():
    def __init__ (self, tLlegada):
        self.tLlegada = tLlegada

    def asignartServicio (self, tServicio):
        self.tServicio = tServicio

    def __str__(self):
        return "{} llego".format(self.tLlegada)