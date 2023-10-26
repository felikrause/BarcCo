
from Parada import Parada


class Ruta:

  def __init__(self, id: int, lugar_salida:Parada , lugar_llegada: Parada):
    self.id = id
    self.lugar_salida = lugar_salida
    self.lugar_llegada = lugar_llegada

  def calcular_costo(self):
    print("Se realiza calcular costo")

  def calcular_gasto(self):
    print("Se realiza calcular gasto")

  def tiene_nafta(self, barco: Barco) -> bool:
    print("Se realiza comprobación de nafta")
    return True
