from typing import List
from Barco import Barco
from Marinero import Marinero
from Parada import Parada


class Viaje:

  def __init__(self, id: int, barco:Barco, marinero: Marinero,
               recorrido: List[Parada]):
    self.id = id
    self.barco = barco
    self.marinero = marinero
    self.recorrido = recorrido

  def calcular_gasto(self):
    print("Se realiza calcular gasto")

  def calcular_costo(self):
    print("Se realiza calcular costo")

  def calcular_tiempo(self):
    print("Se realiza calcular tiempo")
