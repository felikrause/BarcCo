class Barco:
    def __init__(self, id: int, capacidad_maxima: float, capacidad_tanque: float):
        self.id = id
        self.capacidad_maxima = capacidad_maxima
        self.capacidad_tanque = capacidad_tanque

    def consumir_nafta(self):
        print("Se realiza consumir nafta")
      