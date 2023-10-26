class Parada:
    def __init__(self, id: int, tipo: str, fecha_llegada: str, fecha_salida: str):
        self.id = id
        self.tipo = tipo
        self.fecha_llegada = fecha_llegada
        self.fecha_salida = fecha_salida

    def calcular_gasto(self):
      print("Se realiza calcular gasto")
        
    def calcular_costo(self):
      print("Se realiza calcular costo")

    def calcular_tiempo(self):
      print("Se realiza calcular tiempo")